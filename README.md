# Multilingual Hate Speech and Toxic Content Moderation

An advanced moderation pipeline capable of detecting abusive language, hate speech, and toxicity across both user-generated text chat and voice note/audio stream transcripts in multiple languages.

## Features
- **Multilingual Keyword & Semantic Analysis:** Filters toxic content across multiple language distributions.
- **Phonetic Audio Scoring:** Evaluates voice notes and audio chat logs for aggressive speech patterns.
- **FastAPI REST Endpoint:** Built for real-time community safety and chat moderation.

## Project Structure
```text
multilingual_content_moderator/
├── data/
│   └── multilingual_samples.csv
├── src/
│   ├── moderator.py
│   └── app.py
├── requirements.txt
└── README.md
```

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run batch moderation script: `python src/moderator.py`
3. Start API server: `uvicorn src.app:app --reload`
