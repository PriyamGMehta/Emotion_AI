class DataUnderstanding:

    def __init__(self, df):
        self.df = df

    def dataset_shape(self):
        print("\n========== Dataset Shape ==========")
        print(self.df.shape)

    def columns(self):
        print("\n========== Columns ==========")
        print(self.df.columns.tolist())

    def data_types(self):
        print("\n========== Data Types ==========")
        print(self.df.dtypes)

    def missing_values(self):
        print("\n========== Missing Values ==========")
        print(self.df.isnull().sum())

    def duplicate_rows(self):
        print("\n========== Duplicate Rows ==========")
        print(self.df.duplicated().sum())

    def unique_emotions(self):
        print("\n========== Unique Emotions ==========")
        print(self.df["emotion"].unique())

    def emotion_distribution(self):
        print("\n========== Emotion Distribution ==========")
        print(self.df["emotion"].value_counts())

    def sentence_statistics(self):

        sentence_length = self.df["text"].apply(
            lambda x: len(x.split())
        )

        print("\n========== Sentence Statistics ==========")
        print(f"Average Length : {sentence_length.mean():.2f}")
        print(f"Minimum Length : {sentence_length.min()}")
        print(f"Maximum Length : {sentence_length.max()}")

    def generate_report(self):

        self.dataset_shape()
        self.columns()
        self.data_types()
        self.missing_values()
        self.duplicate_rows()
        self.unique_emotions()
        self.emotion_distribution()
        self.sentence_statistics()