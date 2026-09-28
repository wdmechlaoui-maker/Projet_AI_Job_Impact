# Fichier : Visualisations/viz_02_risky_industries.py
import plotly.express as px

def generate_risky_industries_chart(df):
    """
    Génère le Bar Chart horizontal interactif pour les secteurs les plus exposés à l'IA.
    Retourne un objet Figure Plotly.
    """
    fig = px.bar(
        df,
        x="avg_ai_risk",
        y="industry",
        orientation="h",
        text="avg_ai_risk",
        color_discrete_sequence=["#e67e22"]  # Orange pour différencier du KPI 1
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        height=450,
        xaxis_title="Score de risque moyen (0 à 3)",
        yaxis_title="",
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    # Formatage propre du texte (2 décimales) à l'extérieur des barres
    fig.update_traces(
        texttemplate='%{text:.2f}', 
        textposition='outside',
        cliponaxis=False
    )
    
    return fig