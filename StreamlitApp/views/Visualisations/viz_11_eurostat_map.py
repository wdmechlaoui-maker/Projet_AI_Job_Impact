# Fichier : Visualisations/viz_eurostat_map.py
import plotly.express as px

def generate_eurostat_choropleth(df):
    """
    Génère une carte choroplèthe de l'Europe basée sur l'indice de digitalisation Eurostat.
    """
    fig = px.choropleth(
        df,
        locations="country",         # La colonne contenant le nom ou le code du pays
        locationmode="country names", # Dis à Plotly qu'il s'agit des noms complets (ex: 'Germany')
                                     # Change par "ISO-3" si tu as des codes à 3 lettres (ex: DEU)
        color="avg_digitalization",  # La variable qui détermine l'intensité de la couleur
        hover_name="country",        # Nom affiché en grand au survol
        labels={
            "avg_digitalization": "Moyenne de Digitalisation"
        },
        color_continuous_scale="Viridis", # Échelle de couleur pro et très lisible (du jaune au violet/bleu)
        scope="europe"               # <-- CRUCIAL : Centre et zoom automatiquement sur l'Europe !
    )
    
    fig.update_layout(
        height=500,
        margin=dict(l=0, r=0, t=30, b=0),
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    return fig