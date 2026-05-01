# Smart-Email-Summarizer
AI-powered Chrome extension that summarizes Gmail emails using Groq LLM.

## Features
- 📧 Extracts email content from Gmail
- 🤖 AI summarization using LLaMA 3 (Groq)
- ⚡ Fast and real-time summaries
- 🎯 Highlights key points and actions

## Tech Stack
- Frontend: Chrome Extension (HTML, CSS, JS)
- Backend: Flask (Python)
- AI: Groq API

## How It Works
1. Extract email content using content script
2. Send to Flask backend
3. Backend calls Groq API
4. Returns summarized output

## Architecture
Chrome Extension → Flask API → Groq LLM → Response

## Features
- Bullet point summaries
- Action item detection
- Fast inference (Groq)


