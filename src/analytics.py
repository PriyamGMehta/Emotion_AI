import pandas as pd
import plotly.express as px
from sklearn.feature_extraction.text import CountVectorizer
from src.dashboard_utils import DashboardUtils

class Analytics:

    def __init__(self):
        self.utils = DashboardUtils()

    def emotion_statistics(self, df):

        stats = {}

        stats["Total Samples"] = len(df)

        stats["Emotion Classes"] = df["emotion"].nunique()

        stats["Average Sentence Length"] = round(
            df["clean_text"]
            .astype(str)
            .apply(lambda x: len(x.split()))
            .mean(),
            2
        )

        stats["Vocabulary Size"] = (
            df["clean_text"]
            .str.split()
            .explode()
            .nunique()
        )

        return stats


    def emotion_distribution(self, df):

        emotion = (
            df["emotion"]
            .value_counts()
            .reset_index()
        )

        emotion.columns = [
            "Emotion",
            "Count"
        ]

        fig = px.bar(
            emotion,
            x="Emotion",
            y="Count",
            color="Emotion",
            text="Count",
            title="Emotion Distribution",
            color_discrete_sequence=self.utils.saas_colors
        )

        fig.update_layout(
            title_x=0.5,
            **self.utils.layout_config
        )
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="#F3F4F6")

        return fig


    def emotion_pie_chart(self, df):

        emotion = (
            df["emotion"]
            .value_counts()
            .reset_index()
        )

        emotion.columns = [
            "Emotion",
            "Count"
        ]

        fig = px.pie(
            emotion,
            names="Emotion",
            values="Count",
            hole=0.45,
            title="Emotion Percentage",
            color_discrete_sequence=self.utils.saas_colors
        )

        fig.update_layout(
            title_x=0.5,
            **self.utils.layout_config
        )

        return fig


    def sentence_length_distribution(self, df):

        temp = df.copy()

        temp["Sentence Length"] = (
            temp["clean_text"]
            .astype(str)
            .apply(lambda x: len(x.split()))
        )

        fig = px.histogram(
            temp,
            x="Sentence Length",
            nbins=30,
            title="Sentence Length Distribution",
            color_discrete_sequence=[self.utils.saas_colors[0]]
        )

        fig.update_layout(
            title_x=0.5,
            **self.utils.layout_config
        )
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="#F3F4F6")

        return fig


    def top_words(self, df, top_n=20):

        vectorizer = CountVectorizer(
            stop_words="english"
        )

        X = vectorizer.fit_transform(
            df["clean_text"]
        )

        words = vectorizer.get_feature_names_out()

        frequency = X.sum(axis=0).A1

        word_df = pd.DataFrame({
            "Word": words,
            "Frequency": frequency
        })

        word_df = word_df.sort_values(
            by="Frequency",
            ascending=False
        ).head(top_n)

        fig = px.bar(
            word_df,
            x="Frequency",
            y="Word",
            orientation="h",
            color="Frequency",
            title=f"Top {top_n} Most Frequent Words",
            color_continuous_scale="Blues"
        )

        fig.update_layout(
            title_x=0.5,
            yaxis=dict(categoryorder="total ascending"),
            **self.utils.layout_config
        )
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="#F3F4F6")

        return fig