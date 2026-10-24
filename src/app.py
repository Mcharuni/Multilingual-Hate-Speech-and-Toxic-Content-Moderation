from fastapi import FastAPI
from pydantic import BaseModel
from src.moderator import MultilingualContentModerator

app = FastAPI(title="Multilingual Hate Speech Moderation API", version="1.0")
moderator = MultilingualContentModerator()

class ModerationInput(BaseModel):
    content_text: str
    phonetic_toxicity_score: float
    language_code: str = "en"

@app.get("/")
def home():
    return {"message": "Multilingual Hate Speech & Toxic Content Moderation API is online!"}

@app.post("/moderate")
def moderate_content(data: ModerationInput):
    decision, score = moderator.analyze_toxicity(data.content_text, data.phonetic_toxicity_score)
    is_blocked = "Block" in decision
    
    return {
        "language": data.language_code,
        "moderation_action": decision,
        "calculated_toxicity_score": score,
        "action_taken": "Content Removed / Blocked" if is_blocked else "Content Published"
    }
