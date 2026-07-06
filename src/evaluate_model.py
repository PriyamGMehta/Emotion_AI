import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


class ModelEvaluator:

    def evaluate(self, trained_models, X_val, y_val):

        results = []

        best_model = None
        best_score = 0

        for name, model in trained_models.items():

            prediction = model.predict(X_val)

            accuracy = accuracy_score(y_val, prediction)

            precision = precision_score(
                y_val,
                prediction,
                average="weighted"
            )

            recall = recall_score(
                y_val,
                prediction,
                average="weighted"
            )

            f1 = f1_score(
                y_val,
                prediction,
                average="weighted"
            )

            results.append({
                "Model": name,
                "Accuracy": accuracy,
                "Precision": precision,
                "Recall": recall,
                "F1 Score": f1
            })

            if f1 > best_score:

                best_score = f1
                best_model = model

        results = pd.DataFrame(results)

        return results, best_model