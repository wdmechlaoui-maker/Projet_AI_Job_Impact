# Fichier : Visualisations/viz_08_digital_trend.py
import plotly.express as px
import plotly.graph_objects as go

def generate_digital_trend_chart(df):
    """
    Génère un Line Chart interactif avec zone ombrée pour l'évolution temporelle.
    """
    # Sécurité tri par année
    df_sorted = df.sort_values(by="year", ascending=True)
    
    # Utilisation de Graph Objects pour faire l'effet Area Chart propre
    fig = go.Figure()
    
    # Ajout de la ligne avec remplissage en dessous (Ta stratégie visuelle)
    fig.add_trace(go.Scatter(
        x=df_sorted["year"],
        y=df_sorted["avg_digital_score"],
        mode="lines+markers",
        line=dict(color="#2b5c8f", width=3),
        marker=dict(size=8),
        fill='tozeroy',
        fillcolor='rgba(43, 92, 143, 0.1)',  # Bleu Eurostat très transparent
        text=df_sorted["avg_digital_score"].apply(lambda x: f"{x:.1f}%"),
        textposition="top center",
        hovertemplate="<b>Année %{x}</b><br>Score : %{y:.2f}%<extra></extra>"
    ))
    
    # Ajustement des axes pour donner de la respiration
    fig.update_layout(
        xaxis=dict(tickmode='array', tickvals=df_sorted["year"]),
        yaxis=dict(range=[df_sorted["avg_digital_score"].min() - 2, df_sorted["avg_digital_score"].max() + 2]),
        height=400,
        xaxis_title="Année",
        yaxis_title="Score numérique moyen (%)",
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    return fig