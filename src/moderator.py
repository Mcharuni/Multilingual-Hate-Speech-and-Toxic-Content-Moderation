import pandas as pd
import numpy as np

class MultilingualContentModerator:
    def __init__(self, data_path="data/multilingual_samples.csv"):
        self.df = pd.read_csv(data_path)

    def analyze_toxicity(self, text, phonetic_score):
        # Multilingual toxic keyword heuristics (English, Spanish, French, German)
        toxic_triggers = [
            "suffer", "idiota", "desaparecer", "verdammter", "betrüger", 
            "anzeige", "terribly", "idiot", "hate"
        ]
        
        text_lower = text.lower()
        keyword_hits = sum(1 for word in toxic_triggers if word in text_lower)
        
        # Combine keyword matches and phonetic audio toxicity scores
        combined_score = min(1.0, (keyword_hits * 0.4) + (phonetic_score * 0.6))
        
        if combined_score > 0.7:
            return "High Toxicity (Block Content)", round(combined_score, 2)
        elif combined_score > 0.4:
            return "Moderate Toxicity (Flag for Review)", round(combined_score, 2)
        else:
            return "Safe Content (Approved)", round(combined_score, 2)

    def process_batch(self):
        results = []
        for _, row in self.df.iterrows():
            moderation_status, score = self.analyze_toxicity(
                row["content_text"], row["phonetic_toxicity_score"]
            )
            results.append({
                "sample_id": row["sample_id"],
                "language": row["language_code"],
                "content_source": row["context_type"],
                "moderation_decision": moderation_status,
                "toxicity_score": score
            })
        return pd.DataFrame(results)

if __name__ == "__main__":
    moderator = MultilingualContentModerator()
    print(moderator.process_batch())
