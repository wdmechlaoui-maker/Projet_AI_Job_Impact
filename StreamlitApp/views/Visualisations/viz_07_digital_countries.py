# Fichier : Visualisations/viz_07_digital_countries.py
import plotly.express as px

def generate_digital_countries_chart(df):
    """
    Génère le Bar Chart horizontal interactif pour le Top 10 des pays les plus digitalisés.
    Applique un zoom à partir de 60% avec une grille de repère.
    """
    # Tri ascendant pour un affichage propre du bas vers le haut sur l'axe Y
    df_sorted = df.sort_values(by="avg_digital_score", ascending=True)
    
    fig = px.bar(
        df_sorted,
        x="avg_digital_score",
        y="country",
        orientation="h",
        text="avg_digital_score",
        color_discrete_sequence=["#2b5c8f"]  # Bleu Eurostat institutionnel
    )
    
    # Application de ton zoom (60%) et style
    fig.update_layout(
        xaxis=dict(
            range=[60, max(df_sorted["avg_digital_score"]) * 1.05],
            showgrid=True,
            gridcolor="#cccccc",
            gridwidth=1,
            griddash="dash"
        ),
        height=450,
        xaxis_title="Score numérique moyen (%)",
        yaxis_title="",
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    fig.update_traces(
        texttemplate='%{text:.1f}%',
        textposition='outside',
        cliponaxis=False
    )
    
    return fig