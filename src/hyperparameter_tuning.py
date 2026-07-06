from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression


class HyperparameterTuning:

    def tune_svm(self, X_train, y_train):

        parameters = {
            "C": [0.1, 1, 5, 10]
        }

        svm = LinearSVC(
            class_weight="balanced",
            random_state=42
        )

        grid = GridSearchCV(
            estimator=svm,
            param_grid=parameters,
            scoring="f1_weighted",
            cv=5,
            n_jobs=-1
        )

        grid.fit(X_train, y_train)

        print("\nBest Parameters:", grid.best_params_)
        print("Best Score:", grid.best_score_)

        return grid.best_estimator_


    def tune_logistic(self, X_train, y_train):

        parameters = {
            "C": [0.1, 1, 5, 10]
        }

        lr = LogisticRegression(
            max_iter=3000,
            class_weight="balanced",
            random_state=42
        )

        grid = GridSearchCV(
            estimator=lr,
            param_grid=parameters,
            scoring="f1_weighted",
            cv=5,
            n_jobs=-1
        )

        grid.fit(X_train, y_train)

        print("\nBest Parameters:", grid.best_params_)
        print("Best Score:", grid.best_score_)

        return grid.best_estimator_