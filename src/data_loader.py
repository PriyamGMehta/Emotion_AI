import pandas as pd

from src.config import (
    TRAIN_DATA,
    VAL_DATA,
    TEST_DATA
)

class DataLoader:

    @staticmethod
    def load_train():
        return pd.read_csv(
            TRAIN_DATA,
            sep=";",
            names=["text", "emotion"]
        )

    @staticmethod
    def load_validation():
        return pd.read_csv(
            VAL_DATA,
            sep=";",
            names=["text", "emotion"]
        )

    @staticmethod
    def load_test():
        return pd.read_csv(
            TEST_DATA,
            sep=";",
            names=["text", "emotion"]
        )