# Fichier : Visualisations/viz_05_salary_impact.py
import plotly.express as px

def generate_salary_chart(df):
    """
    Génère le graphique Plotly interactif pour l'impact des salaires.
    Prend en entrée le DataFrame extrait de la BDD.
    Retourne un objet Figure Plotly.
    """
    fig = px.bar(
        df,
        x="job_role",
        y=["avg_salary_before", "avg_salary_after"], 
        barmode="group",
        color_discrete_sequence=["#7f8c8d", "#2e7d32"] # Gris sobre vs Vert croissance
    )

    fig.update_layout(
        height=500,
        xaxis_title="",
        yaxis_title="Salaire moyen ($)",
        legend_title_text="Période",
        margin=dict(l=20, r=20, t=30, b=20)
    )
    
    # On renvoie la figure au lieu de l'afficher
    return fig