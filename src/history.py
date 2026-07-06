import os
from datetime import datetime

import pandas as pd


class PredictionHistory:

    def __init__(self):

        self.file_path = "outputs/predictions/history.csv"

        os.makedirs(
            "outputs/predictions",
            exist_ok=True
        )

        if not os.path.exists(self.file_path):

            pd.DataFrame(
                columns=[
                    "Time",
                    "Text",
                    "Emotion",
                    "Emoji",
                    "Prediction Time"
                ]
            ).to_csv(
                self.file_path,
                index=False
            )

    def save(
        self,
        text,
        emotion,
        emoji,
        prediction_time
    ):

        history = pd.read_csv(
            self.file_path
        )

        new_row = pd.DataFrame({

            "Time":[
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )
            ],

            "Text":[text],

            "Emotion":[emotion],

            "Emoji":[emoji],

            "Prediction Time":[prediction_time]

        })

        history = pd.concat(
            [
                history,
                new_row
            ],
            ignore_index=True
        )

        history.to_csv(
            self.file_path,
            index=False
        )

    def load(self):

        return pd.read_csv(
            self.file_path
        )

    def clear(self):

        pd.DataFrame(
            columns=[
                "Time",
                "Text",
                "Emotion",
                "Emoji",
                "Prediction Time"
            ]
        ).to_csv(
            self.file_path,
            index=False
        )