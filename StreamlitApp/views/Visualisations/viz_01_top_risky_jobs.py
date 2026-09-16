# Fichier : Visualisations/viz_01_top_risky_jobs.py
import plotly.express as px

def generate_top_risky_jobs_chart(df):
    """
    Génère le Bar Chart horizontal interactif pour le Top 10 des métiers exposés à l'IA.
    Retourne un objet Figure Plotly.
    """
    fig = px.bar(
        df,
        x="avg_ai_risk",
        y="job_role",
        orientation="h",
        text="avg_ai_risk",
        color_discrete_sequence=["#e74c3c"]  # Rouge alerte pour l'exposition au risque
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        height=450,
        xaxis_title="Score de risque moyen (0 à 1)",
        yaxis_title="",
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor="rgba(0,0,0,0)"  # Fond épuré
    )
    
    # Formatage propre du texte sur les barres (2 décimales)
    fig.update_traces(
        texttemplate='%{text:.2f}', 
        textposition='outside',
        cliponaxis=False
    )

    return fig
    