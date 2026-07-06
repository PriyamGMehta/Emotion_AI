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

    def grouped_bar_chart(self):
        # Melt the dataframe so we have Model, Metric, Value columns
        melted_df = self.df.melt(
            id_vars=['Model'], 
            value_vars=['Accuracy', 'Precision', 'Recall', 'F1 Score'],
            var_name='Metric', 
            value_name='Score'
        )
        
        # Use a sleek dark blue/purple color scheme to match the Neural Core theme
        fig = px.bar(
            melted_df,
            x="Metric",
            y="Score",
            color="Model",
            barmode="group",
            text="Score",
            title="Model Performance Comparison",
            color_discrete_sequence=['#3B82F6', '#10B981', '#8B5CF6']
        )
        
        # Format the text on the bars to 3 decimals
        fig.update_traces(texttemplate='%{text:.3f}', textposition='outside')
        
        # Update layout to look premium
        fig.update_layout(
            title_x=0.5,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Space Grotesk"),
            yaxis=dict(
                title="Score",
                range=[0.0, 1.1],
                gridcolor='rgba(0,0,0,0.1)'
            ),
            xaxis=dict(
                title="",
                gridcolor='rgba(0,0,0,0.0)'
            ),
            legend_title_text="Model",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )
        
        return fig