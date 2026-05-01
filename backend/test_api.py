import requests

url = "http://127.0.0.1:5000/summarize"

data = {
    "text": """Hi team,
    We have a client meeting tomorrow at 10 AM.
    Please prepare the presentation slides.
    Also, send the final report before tonight.
    Thanks."""
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())