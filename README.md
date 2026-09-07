# Smart-Email-Summarizer

AI-powered Chrome extension that summarizes Gmail emails using Groq LLM.

## Features

* 📧 Extracts email content from Gmail
* 🤖 AI summarization using LLaMA 3 (Groq)
* ⚡ Fast and real-time summaries
* 🎯 Highlights key points and actions

## Tech Stack

* Frontend: Chrome Extension (HTML, CSS, JS)
* Backend: Flask (Python)
* AI: Groq API

## How It Works

1. Extract email content using content script
2. Send to Flask backend
3. Backend calls Groq API
4. Returns summarized output

## Architecture

Chrome Extension → Flask API → Groq LLM → Response

## Features

* Bullet point summaries
* Action item detection
* Fast inference (Groq)







\## ⚙️ Installation \& Setup



Follow these steps to run the Smart Email Summarizer locally.



\### 1. Clone the Repository

git clone https://github.com/AyushShahir/Smart-Email-Summarizer.git

cd Smart-Email-Summarizer





\### 2. Create a Virtual Environment

python -m venv venv





Activate the virtual environment on Windows:

venv\\Scripts\\activate





\### 3. Install Dependencies

pip install -r backend/requirements.txt





\### 4. Configure the Groq API Key

Create a `.env` file inside the `backend` folder:

GROQ\_API\_KEY=your\_groq\_api\_key





Replace `your\_groq\_api\_key` with your actual Groq API key.



> ⚠️ Never commit your `.env` file or expose your API key publicly.



\### 5. Start the Backend

python backend/app.py



The Flask backend will start locally.



\### 6. Load the Chrome Extension



1\. Open Google Chrome.

2\. Go to `chrome://extensions/`.

3\. Enable \*\*Developer mode\*\*.

4\. Click \*\*Load unpacked\*\*.

5\. Select the project's `extension` folder.

6\. Open Gmail and use the Smart Email Summarizer extension.



\---



\## 📁 Project Structure





Smart-Email-Summarizer/

│

├── backend/

│   ├── app.py

│   └── requirements.txt

│

├── extension/

│   ├── manifest.json

│   ├── popup.html

│   ├── popup.js

│   ├── content.js

│   └── styles.css

│

├── .gitignore

└── README.md



