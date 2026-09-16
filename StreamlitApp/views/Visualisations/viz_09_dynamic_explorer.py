# Fichier : Visualisations/viz_06_dynamic_explorer.py
import plotly.express as px

def generate_dynamic_bubble_chart(df):
    """
    Génère le bubble chart épuré avec des tailles de bulles proportionnelles et contrastées.
    """
    # Étape de sécurité : s'assurer que les volumes de postes sont bien numériques
    df["job_openings"] = df["job_openings"].astype(float)
    
    # 🌟 CORRECTION DU DIAMÈTRE MAX : On monte à 90 pour laisser respirer le contraste
    DIAMETRE_MAX = 50
    
    # CALCUL DYNAMIQUE DU SIZEREF : Basé sur le nouveau diamètre maximal
    max_openings = df["job_openings"].max() if not df.empty else 1
    size_reference = 2 * max_openings / (DIAMETRE_MAX**2) 

    fig = px.scatter(
        df,
        x="salary",
        y="ai_risk_score",
        size="job_openings",       # Détermine la taille de la bulle
        color="risk_level",        # Détermine la couleur de la bulle (Low, Medium, High Risk)
        hover_name="job_title",    # Affiche le métier en titre au survol
        size_max=DIAMETRE_MAX,     # 🌟 Application dynamique du nouveau diamètre maximum
        labels={
            "salary": "Salaire Moyen ($)",
            "ai_risk_score": "Score de Risque IA",
            "risk_level": "Niveau de Risque",
            "job_openings": "Postes Ouverts"
        },
        hover_data={
            "salary": ":$,.0f",
            "job_openings": ":,.",
            "experience_level": True
        },
        color_discrete_map={
            "High Risk": "#EF4444",    # Rouge vif et pro
            "Medium Risk": "#F59E0B",  # Orange vif et pro
            "Low Risk": "#10B981"      # Vert vif et pro
        },
        category_orders={"risk_level": ["Low Risk", "Medium Risk", "High Risk"]}
    )
    
    # Force l'ajustement mathématique des tailles pour éliminer l'effet "toutes identiques"
    fig.update_traces(
        marker=dict(
            sizeref=size_reference,
            sizemode="area",        # L'aire est proportionnelle à la valeur (standard pro)
            line=dict(width=1.2, color="White")
        ),
        opacity=0.85                # Excellente visibilité des superpositions
    )
    
    fig.update_layout(
        height=550,
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    fig.update_xaxes(showgrid=True, gridcolor="#f3f4f6")
    fig.update_yaxes(showgrid=True, gridcolor="#f3f4f6")
    
    return fig