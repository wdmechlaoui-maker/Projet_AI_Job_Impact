# Fichier : Visualisations/viz_06_upskilling_jobs.py
import plotly.graph_objects as go

def generate_upskilling_chart(df):
    """
    Génère le Lollipop Chart interactif avec Plotly pour le taux d'upskilling.
    Retourne un objet Figure Plotly.
    """
    # Tri pour garantir un affichage ascendant propre sur l'axe Y
    df_sorted = df.sort_values(by="upskilling_rate", ascending=True)
    
    fig = go.Figure()
    
    # 1. Ajout des tiges du Lollipop
    for i in range(len(df_sorted)):
        job = df_sorted["job_role"].iloc[i]
        rate = df_sorted["upskilling_rate"].iloc[i]
        
        fig.add_shape(
            type="line",
            x0=0,
            x1=rate,
            y0=job,
            y1=job,
            line=dict(color="#4a69bd", width=2)
        )
        
    # 2. Ajout des points (marqueurs) interactifs
    fig.add_trace(
        go.Scatter(
            x=df_sorted["upskilling_rate"],
            y=df_sorted["job_role"],
            mode="markers+text",
            marker=dict(color="#4a69bd", size=14),
            text=df_sorted["upskilling_rate"].apply(lambda x: f" {x:.1f}%"),
            textposition="middle right",
            textfont=dict(weight="bold"),
            hovertemplate="<b>%{y}</b><br>Taux d'upskilling : %{x:.1f}%<extra></extra>",
            showlegend=False
        )
    )
    
    # 3. Ligne de repère pour la moyenne globale du Top 10
    mean_rate = df_sorted["upskilling_rate"].mean()
    fig.add_vline(
        x=mean_rate, 
        line_width=1.5, 
        line_dash="dash", 
        line_color="#e67e22",
        annotation_text=f"Moyenne Top 10: {mean_rate:.1f}%",
        annotation_position="bottom right"
    )
    
    # Mise en forme du layout
    fig.update_layout(
        xaxis_title="Upskilling Rate (%)",
        yaxis_title="",
        xaxis=dict(range=[0, max(df_sorted["upskilling_rate"]) * 1.15]),
        height=500,
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    return fig