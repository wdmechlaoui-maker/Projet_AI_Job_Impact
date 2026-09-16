# Fichier : Visualisations/viz_06_heatmap.py
import plotly.express as px

def generate_risk_heatmap(df):
    """
    Génère un Heatmap pro : Pays en X, Niveau de Risque en Y, 
    et le volume de postes en intensité de couleur.
    """
    # Pivot des données pour s'assurer que Plotly l'affiche comme une vraie matrice
    # Si px.density_heatmap est utilisé, il gère l'agrégation en direct
    fig = px.density_heatmap(
        df,
        x="country",
        y="risk_level",
        z="total_openings",
        labels={
            "country": "Pays",
            "risk_level": "Niveau de Risque IA",
            "total_openings": "Total des Postes"
        },
        category_orders={
            "risk_level": ["Low Risk", "Medium Risk", "High Risk"] # Ordre logique du bas vers le haut
        },
        color_continuous_scale="YlOrRd", # Couleurs chaudes pour simuler la "densité/menace"
        text_auto=True # Affiche directement les chiffres dans les cases, ultra pro !
    )
    
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=True
    )
    
    return fig