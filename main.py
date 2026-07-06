import pandas as pd
from src.data_loader import DataLoader
from src.data_understanding import DataUnderstanding
from src.preprocessing import TextPreprocessor
from src.visualization import Visualization
from src.feature_engineering import FeatureEngineering
from src.train_model import ModelTrainer
from src.evaluate_model import ModelEvaluator
from src.hyperparameter_tuning import HyperparameterTuning
from src.test_model import TestModel
from src.predict import EmotionPredictor


def main():

    train_df = DataLoader.load_train()
    val_df = DataLoader.load_validation()
    test_df = DataLoader.load_test()

    print("=" * 50)
    print("TRAIN DATASET")
    print("=" * 50)

    print(train_df.head())
    print("\nShape:", train_df.shape)

    print("\n" + "=" * 50)
    print("VALIDATION DATASET")
    print("=" * 50)

    print(val_df.head())
    print("\nShape:", val_df.shape)

    print("\n" + "=" * 50)
    print("TEST DATASET")
    print("=" * 50)

    print(test_df.head())
    print("\nShape:", test_df.shape)


    analysis = DataUnderstanding(train_df)
    analysis.generate_report()

    # ==========================
    # Text Preprocessing
    # ==========================

    train_df = pd.read_csv("data/processed/train_clean.csv")
    val_df = pd.read_csv("data/processed/val_clean.csv")
    test_df = pd.read_csv("data/processed/test_clean.csv")
    print("\nPreprocessing Completed Successfully!\n")
    print(
        train_df[
            ["text", "clean_text", "emotion"]
        ].head()
    )

    # train_df.to_csv(
    #     "data/processed/train_clean.csv",
    #     index=False
    # )

    # val_df.to_csv(
    #     "data/processed/val_clean.csv",
    #     index=False
    # )

    # test_df.to_csv(
    #     "data/processed/test_clean.csv",
    #     index=False
    # )

    # print("\nClean datasets saved successfully!")

    # ==============================
    # Exploratory Data Analysis
    # ==============================

    # visual = Visualization()
    # visual.emotion_distribution(train_df)
    # visual.emotion_pie_chart(train_df)
    # visual.sentence_length_distribution(train_df)
    # visual.word_cloud(train_df)
    # print("\nEDA Completed Successfully!")

    # ==============================
    # Feature Engineering
    # ==============================

    feature = FeatureEngineering()

    # TF-IDF
    X_train = feature.fit_tfidf(train_df["clean_text"])
    X_val = feature.transform_tfidf(val_df["clean_text"])
    X_test = feature.transform_tfidf(test_df["clean_text"])

    # Labels
    y_train = train_df["emotion"]
    y_val = val_df["emotion"]
    y_test = test_df["emotion"]

    # Save Vectorizers
    feature.save_vectorizers()

    print("\n========== Feature Engineering ==========")

    print("Train Feature Shape :", X_train.shape)
    print("Validation Feature Shape :", X_val.shape)
    print("Test Feature Shape :", X_test.shape)

    print("\nVectorizers saved successfully!")

    # ==============================
    # Model Training
    # ==============================

    trainer = ModelTrainer()

    trained_models = trainer.train_models(
        X_train,
        y_train
    )

    print("\nAll models trained successfully!")

    # ==============================
    # Model Evaluation
    # ==============================

    evaluator = ModelEvaluator()

    results, best_model = evaluator.evaluate(
        trained_models,
        X_val,
        y_val
    )

    print("\n========== MODEL COMPARISON ==========\n")

    print(results)

    results.to_csv(
        "outputs/reports/model_comparison.csv",
        index=False
    )

    trainer.save_model(
        best_model,
        "best_emotion_model"
    )

    print("\nBest model saved successfully!")

    # ==========================
    # Hyperparameter Tuning
    # ==========================

    tuner = HyperparameterTuning()

    best_svm = tuner.tune_svm(
        X_train,
        y_train
    )

    trainer.save_model(
        best_svm,
        "best_emotion_model"
    )

    print("\nBest tuned model saved successfully!")

    # ==========================
    # Final Test Evaluation
    # ==========================

    tester = TestModel()

    tester.evaluate(
        X_test,
        y_test
    )

    # ==========================
    # Emotion Prediction
    # ==========================

    predictor = EmotionPredictor()

    while True:

        text = input("\nEnter Text (type 'exit' to quit): ")

        if text.lower() == "exit":
            break

        emotion, emoji = predictor.predict(text)

        print("\nPrediction Result")
        print("----------------------------")
        print(f"Emotion : {emotion}")
        print(f"Emoji   : {emoji}")

if __name__ == "__main__":
    main()