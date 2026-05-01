from flask import Flask, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)

CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")
    language = data.get("language", "English")

    if not text:
        return jsonify({"summary": "No email content found"}), 400

    # limit long emails (important)
    text = text[:4000]

    try:
        response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": f"Summarize the email in {language} in 3-4 clear bullet points. Do not use markdown symbols like * or **. Keep it clean and readable."
        },
        {
            "role": "user",
            "content": text
        }
    ],
    temperature=0.1
)

        summary = response.choices[0].message.content

        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"summary": str(e)}), 500

@app.route("/")
def home():
    return "AI Email Summarizer API is running!"



if __name__ == "__main__":
    app.run(debug=True)