
import streamlit as st
from utils.ui import load_global_css
import plotly.express as px
import plotly.graph_objects as go
from controllers.ai_controller import (
    get_top_risky_jobs,
    get_risky_industries,
    get_salary_impact,
    get_upskilling
)
import os
import sys
from pathlib import Path
from views.Visualisations.viz_01_top_risky_jobs import generate_top_risky_jobs_chart
from views.Visualisations.viz_02_risky_industries import generate_risky_industries_chart
from views.Visualisations.viz_05_salary_impact import generate_salary_chart
from views.Visualisations.viz_06_upskilling_jobs import generate_upskilling_chart

# Détermination du chemin vers la racine réelle du projet (ProjetVersion1)
root_path = Path(__file__).resolve().parent.parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))



def show():
    st.title("💡 Analyse de l'Impact de l'IA")

    st.markdown("""
    Analyse dynamique des métiers et secteurs les plus exposés 
    à l'intelligence artificielle, des évolutions salariales et des besoins de formation.
    """)

    # Récupération des données via le Controller
    df_jobs = get_top_risky_jobs()
    df_industries = get_risky_industries()
    df_salary = get_salary_impact()
    df_upskilling = get_upskilling()

    # KPI Métriques en haut de page
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="Métier le plus exposé",
            value=df_jobs.iloc[0]["job_role"] if not df_jobs.empty else "N/A"
        )
    with col2:
        st.metric(
            label="Secteur le plus exposé",
            value=df_industries.iloc[0]["industry"] if not df_industries.empty else "N/A"
        )

    st.markdown("---")

    # =========================================================================================
    # Visualisation KPI 1 : Métiers exposés
    # =========================================================================================
    st.subheader("🎯 Top 10 Most AI-Exposed Jobs")

    # 1. Données dynamiques du Controller
    df_jobs = get_top_risky_jobs()

    # 2. Appel de la fonction graphique importée
    fig_jobs = generate_top_risky_jobs_chart(df_jobs)

    # 3. Affichage Streamlit
    st.plotly_chart(fig_jobs, use_container_width=True)

    st.info("""
    **Enseignement :** Teacher apparaît comme le métier le plus exposé à l'automatisation, suivi de SEO Specialist et Accountant.
    Ces professions comportent une forte proportion de tâches standardisées ou assistables par l'intelligence artificielle.
    """)

    st.markdown("---")

    # =========================================================================================
    # Visualisation KPI 2 : Industries exposées
    # =========================================================================================
    st.subheader("🏢 Industries Most Exposed to AI")
    
    # 1. Données dynamiques du Controller
    df_industries = get_risky_industries()

    # 2. Appel de la fonction graphique importée
    fig_industries = generate_risky_industries_chart(df_industries)

    # 3. Affichage dynamique via Streamlit
    st.plotly_chart(fig_industries, use_container_width=True)

    st.info("""
    **Enseignement :** Le secteur Marketing présente le niveau d'exposition le plus élevé.
    Les secteurs Finance, IT et Education suivent avec des niveaux relativement proches, traduisant une transformation généralisée des activités intellectuelles par l'IA.
    """)

    st.markdown("---")

    # =========================================================================================
    # Visualisation KPI 5 : Impact sur les salaires (CORRIGÉ)
    # =========================================================================================
    
    st.subheader("💰 Salary Impact")

    # 1. Récupération des données dynamiques via ton contrôleur
    df_salary = get_salary_impact()

    # 2. Génération du graphique Plotly depuis ton dossier Visualisations
    fig_salary = generate_salary_chart(df_salary)

    # 3. Affichage interactif natif dans Streamlit
    st.plotly_chart(fig_salary, use_container_width=True)

    st.info("""
    **Enseignement :** Les métiers étudiés affichent tous une progression salariale après
    l'intégration de l'IA. Les professions médicales (Doctor, Nurse)
    enregistrent les gains moyens les plus élevés, suggérant que l'IA
    agit davantage comme un levier d'augmentation de productivité que
    comme un substitut direct dans ces domaines.
    """
    )
    st.markdown("--")

    # =========================================================================================
    # Visualisation KPI 6 : Upskilling Lollipop (CORRIGÉ)
    # =========================================================================================
    st.subheader("📚 Upskilling Requirements")

    # L'IMPORT DE TA NOUVELLE FONCTION LOLLIPOP :

    # 1. Récupération des données via le Controller
    df_upskilling = get_upskilling()

    # 2. Génération du graphique Plotly depuis ton dossier Visualisations
    fig_up = generate_upskilling_chart(df_upskilling)

    # 3. Affichage interactif natif dans Streamlit
    st.plotly_chart(fig_up, use_container_width=True)

    st.info("""
    **Enseignement :** Les besoins de montée en compétences dépassent 50 % pour l'ensemble des métiers du classement.
    DevOps Engineer, Content Creator et Quality Inspector apparaissent comme les professions nécessitant les efforts
    de reconversion les plus importants face aux transformations induites par l'IA.""")


