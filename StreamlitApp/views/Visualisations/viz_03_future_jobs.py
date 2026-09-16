# Fichier : Visualisations/viz_03_future_jobs.py
import plotly.express as px

def generate_future_jobs_chart(df):
    """
    Génère un Bar Chart horizontal interactif pour le Top 10 des métiers d'avenir.
    Mets en valeur la croissance de la demande.
    """
    # CORRECTION 1 : Tri sur 'demand_growth' (le nom généré par ton SQL)
    df_sorted = df.sort_values(by="demand_growth", ascending=True)
    
    fig = px.bar(
        df_sorted,
        x="demand_growth",  # Nom de la colonne SQL pour l'axe X
        y="job_title",      # CORRECTION 2 : 'job_title' à la place de 'job_role' pour matcher ton SQL
        orientation="h",
        text="demand_growth",
        color_discrete_sequence=["#2ecc71"]  # Vert opportunité / croissance
    )
    
    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        height=450,
        xaxis_title="Volume total des ouvertures de postes (Demande)",
        yaxis_title="",
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    # On retire le symbole '%' ici car ton SQL fait un SUM(job_openings), 
    # c'est donc un nombre entier de postes ouverts, pas un pourcentage.
    fig.update_traces(
        texttemplate='%{text:,}', # Formate les grands nombres proprement (ex: 10,000)
        textposition='outside',
        cliponaxis=False
    )
    
    return fig