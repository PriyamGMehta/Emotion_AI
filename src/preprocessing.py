import re
import string
import contractions
import nltk
import spacy

from nltk.corpus import stopwords

class TextPreprocessor:

    def __init__(self):
        import spacy
        from nltk.corpus import stopwords
        import nltk
        
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            import subprocess
            subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
            self.nlp = spacy.load("en_core_web_sm")
            
        nltk.download("stopwords", quiet=True)
        self.STOP_WORDS = set(stopwords.words("english"))

    def lowercase(self, text):
        return text.lower()

    def expand_contractions(self, text):
        return contractions.fix(text)

    def remove_urls(self, text):
        return re.sub(r"http\S+|www\S+", "", text)

    def remove_html(self, text):
        return re.sub(r"<.*?>", "", text)

    def remove_numbers(self, text):
        return re.sub(r"\d+", "", text)

    def remove_punctuation(self, text):
        return text.translate(
            str.maketrans("", "", string.punctuation)
        )

    def remove_extra_spaces(self, text):
        return " ".join(text.split())

    def remove_stopwords(self, text):

        words = text.split()

        words = [
            word
            for word in words
            if word not in self.STOP_WORDS
        ]

        return " ".join(words)

    def lemmatize(self, text):

        doc = self.nlp(text)

        return " ".join(
            token.lemma_
            for token in doc
        )

    def preprocess(self, text):

        text = self.lowercase(text)

        text = self.expand_contractions(text)

        text = self.remove_urls(text)

        text = self.remove_html(text)

        text = self.remove_numbers(text)

        text = self.remove_punctuation(text)

        text = self.remove_extra_spaces(text)

        text = self.remove_stopwords(text)

        text = self.lemmatize(text)

        return text

    def process_dataframe(self, df):

        df = df.copy()

        df.drop_duplicates(inplace=True)

        df["clean_text"] = df["text"].apply(
            self.preprocess
        )

        return df