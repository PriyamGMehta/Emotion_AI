import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


class TestModel:

    def evaluate(self, X_test, y_test):

        model = joblib.load(
            "outputs/models/best_emotion_model.pkl"
        )

        prediction = model.predict(X_test)

        print("\n========== FINAL TEST RESULTS ==========\n")

        print("Accuracy :", accuracy_score(y_test, prediction))

        print(
            "Precision :",
            precision_score(
                y_test,
                prediction,
                average="weighted"
            )
        )

        print(
            "Recall :",
            recall_score(
                y_test,
                prediction,
                average="weighted"
            )
        )

        print(
            "F1 Score :",
            f1_score(
                y_test,
                prediction,
                average="weighted"
            )
        )

        print("\nClassification Report:\n")

        print(
            classification_report(
                y_test,
                prediction
            )
        )

        print("\nConfusion Matrix:\n")

        print(
            confusion_matrix(
                y_test,
                prediction
            )
        )