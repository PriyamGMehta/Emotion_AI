import pandas as pd
import plotly.express as px


class ModelComparison:

    def __init__(self):

        self.df = pd.read_csv(
            "outputs/reports/model_comparison.csv"
        )

    def get_data(self):
        return self.df

    def best_model(self):

        return self.df.loc[
            self.df["Accuracy"].idxmax()
        ]

    def accuracy_chart(self):

        fig = px.bar(
            self.df,
            x="Model",
            y="Accuracy",
            color="Model",
            text="Accuracy",
            title="Accuracy Comparison"
        )

        fig.update_layout(
            title_x=0.5,
            template="plotly_white"
        )

        return fig

    def precision_chart(self):

        fig = px.bar(
            self.df,
            x="Model",
            y="Precision",
            color="Model",
            text="Precision",
            title="Precision Comparison"
        )

        fig.update_layout(
            title_x=0.5,
            template="plotly_white"
        )

        return fig

    def recall_chart(self):

        fig = px.bar(
            self.df,
            x="Model",
            y="Recall",
            color="Model",
            text="Recall",
            title="Recall Comparison"
        )

        fig.update_layout(
            title_x=0.5,
            template="plotly_white"
        )

        return fig

    def f1_chart(self):

        fig = px.bar(
            self.df,
            x="Model",
            y="F1 Score",
            color="Model",
            text="F1 Score",
            title="F1 Score Comparison"
        )

        fig.update_layout(
            title_x=0.5,
            template="plotly_white"
        )

        return fig