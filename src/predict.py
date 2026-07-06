import time
import joblib

from src.preprocessing import TextPreprocessor
from src.emoji_mapper import EMOJI_MAP


class EmotionPredictor:

    def __init__(self):

        self.model = joblib.load(
            "outputs/models/best_emotion_model.pkl"
        )

        self.vectorizer = joblib.load(
            "models/tfidf_vectorizer.pkl"
        )

        self.preprocessor = TextPreprocessor()

    def predict(self, text):

        start = time.time()

        clean = self.preprocessor.preprocess(text)

        vector = self.vectorizer.transform([clean])

        emotion = self.model.predict(vector)[0]
        
        # Calculate Confidence Score
        probability = 1.0
        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(vector)[0]
            probability = max(probs)

        end = time.time()

        return {
            "emotion": emotion,
            "emoji": EMOJI_MAP.get(emotion, "❓"),
            "probability": round(probability * 100, 2),
            "clean_text": clean,
            "prediction_time": round(end-start,4)
        }