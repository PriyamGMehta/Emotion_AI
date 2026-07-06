import matplotlib.pyplot as plt
from wordcloud import WordCloud


class Visualization:

    def emotion_distribution(self, df):

        plt.figure(figsize=(8,5))

        df["emotion"].value_counts().plot(
            kind="bar"
        )

        plt.title("Emotion Distribution")
        plt.xlabel("Emotion")
        plt.ylabel("Count")

        plt.tight_layout()

        plt.savefig(
            "outputs/figures/emotion_distribution.png"
        )

        plt.show()


    def emotion_pie_chart(self, df):

        plt.figure(figsize=(7,7))

        df["emotion"].value_counts().plot(
            kind="pie",
            autopct="%1.1f%%"
        )

        plt.ylabel("")

        plt.title("Emotion Percentage")

        plt.tight_layout()

        plt.savefig(
            "outputs/figures/emotion_pie_chart.png"
        )

        plt.show()


    def sentence_length_distribution(self, df):

        df["sentence_length"] = df["clean_text"].apply(
            lambda x: len(x.split())
        )

        plt.figure(figsize=(8,5))

        plt.hist(
            df["sentence_length"],
            bins=30
        )

        plt.title("Sentence Length Distribution")

        plt.xlabel("Sentence Length")

        plt.ylabel("Frequency")

        plt.tight_layout()

        plt.savefig(
            "outputs/figures/sentence_length_distribution.png"
        )

        plt.show()


    def word_cloud(self, df):

        text = " ".join(df["clean_text"])

        wc = WordCloud(
            width=1200,
            height=600,
            background_color="white"
        ).generate(text)

        plt.figure(figsize=(12,6))

        plt.imshow(wc)

        plt.axis("off")

        plt.tight_layout()

        plt.savefig(
            "outputs/figures/word_cloud.png"
        )

        plt.show()