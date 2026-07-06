import plotly.express as px

class DashboardUtils:

    def __init__(self):
        # Clean Enterprise Color Palette
        self.saas_colors = ["#3B82F6", "#6366F1", "#8B5CF6", "#14B8A6", "#F43F5E", "#F59E0B"]
        
        # Universal Chart Styling
        self.layout_config = {
            "font": dict(family="Space Grotesk, sans-serif", color="#1F2937"),
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "margin": dict(t=50, b=30, l=30, r=30)
        }

    def emotion_bar_chart(self, df):

        emotion = df["emotion"].value_counts().reset_index()
        emotion.columns = ["Emotion", "Count"]

        fig = px.bar(
            emotion,
            x="Emotion",
            y="Count",
            color="Emotion",
            text="Count",
            title="Emotion Distribution",
            color_discrete_sequence=self.saas_colors
        )

        fig.update_layout(
            **self.layout_config,
            title_x=0.5,
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, title=""),
            yaxis=dict(showgrid=True, gridcolor="#E5E7EB", zeroline=False, title="")
        )
        
        # Style the bar text
        fig.update_traces(textfont_size=14, textfont_color="#4B5563", textposition="outside")

        return fig

    def emotion_pie_chart(self, df):

        emotion = df["emotion"].value_counts().reset_index()
        emotion.columns = ["Emotion", "Count"]

        fig = px.pie(
            emotion,
            names="Emotion",
            values="Count",
            hole=0.55, 
            title="Emotion Percentage",
            color_discrete_sequence=self.saas_colors
        )

        fig.update_layout(
            **self.layout_config,
            title_x=0.5,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
        )
        
        # Style the donut traces
        fig.update_traces(textinfo='percent', textfont_size=14, textfont_color="#FFFFFF", marker=dict(line=dict(color='#FFFFFF', width=2)))

        return fig