import os
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

class ModelTrainer:
    def __init__(self):
        self.models = {
            "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
            "Naive Bayes": MultinomialNB(),
            "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
        }

    def train_models(self, X_train, y_train):
        trained_models = {}
        for name, model in self.models.items():
            print(f"Training {name}...")
            model.fit(X_train, y_train)
            trained_models[name] = model
        return trained_models

    def save_model(self, model, filename):
        os.makedirs("outputs/models", exist_ok=True)
        filepath = os.path.join("outputs", "models", f"{filename}.pkl")
        joblib.dump(model, filepath)
