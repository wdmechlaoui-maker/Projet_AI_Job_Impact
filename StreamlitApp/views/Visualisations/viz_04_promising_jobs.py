# Fichier : Visualisations/viz_04_promising_jobs.py
import plotly.express as px

def generate_promising_jobs_chart(df):
    """
    Génère un Scatter Plot interactif croisant le salaire et le risque IA 
    pour identifier les meilleurs compromis de carrière.
    """
    fig = px.scatter(
        df,
        x="avg_ai_risk",
        y="avg_salary",
        text="job_title",       # CORRIGÉ : job_title au lieu de job_role
        size="avg_salary",  
        color="avg_salary", 
        color_continuous_scale=px.colors.sequential.YlGnBu,
        hover_name="job_title"  # CORRIGÉ : job_title au lieu de job_role
    )
    
    fig.update_traces(textposition='top center')
    
    fig.update_layout(
        height=500,
        xaxis_title="Score de risque IA (Plus bas = Moins risqué)",
        yaxis_title="Salaire Moyen ($)",
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=True
    )
    
    # Grille de lecture discrète
    fig.update_xaxes(showgrid=True, gridcolor="#f0f0f0")
    fig.update_yaxes(showgrid=True, gridcolor="#f0f0f0")
    
    return fig