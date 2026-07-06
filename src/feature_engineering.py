from sklearn.feature_extraction.text import (
    TfidfVectorizer,
    CountVectorizer
)
import joblib


class FeatureEngineering:

    def __init__(self):

        self.tfidf = TfidfVectorizer(
            max_features=10000,
            ngram_range=(1, 2),
            min_df=2,
            max_df=0.95,
            sublinear_tf=True
        )

        self.count_vectorizer = CountVectorizer(
            max_features=10000,
            ngram_range=(1, 2)
        )

    # -----------------------------
    # TF-IDF
    # -----------------------------
    def fit_tfidf(self, text):
        return self.tfidf.fit_transform(text)

    def transform_tfidf(self, text):
        return self.tfidf.transform(text)

    # -----------------------------
    # Count Vectorizer
    # -----------------------------
    def fit_count(self, text):
        return self.count_vectorizer.fit_transform(text)

    def transform_count(self, text):
        return self.count_vectorizer.transform(text)

    # -----------------------------
    # Save Vectorizers
    # -----------------------------
    def save_vectorizers(self):

        joblib.dump(
            self.tfidf,
            "models/tfidf_vectorizer.pkl"
        )

        joblib.dump(
            self.count_vectorizer,
            "models/count_vectorizer.pkl"
        )