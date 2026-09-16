# Fichier : StreamlitApp/views/explorer_view.py
import streamlit as st
from utils.ui import load_global_css
from controllers.ai_controller import (get_dynamic_explorer, get_heatmap, get_eurostat_map)
from views.Visualisations.viz_09_dynamic_explorer import generate_dynamic_bubble_chart
from views.Visualisations.viz_10_heatmap import generate_risk_heatmap
from views.Visualisations.viz_11_eurostat_map import generate_eurostat_choropleth 

import sqlite3
import pandas as pd
import os
import sys
from pathlib import Path

# Détermination du chemin vers la racine réelle du projet
root_path = Path(__file__).resolve().parent.parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))


def show():
    # =========================================================================
    # EN-TÊTE PRINCIPAL DE LA PAGE
    # =========================================================================
    st.title("🔮 Explorateur Dynamique des Métiers")
    st.markdown(" #### Simulation et analyse croisée : Salaires, Recrutement et Risques d'automatisation")
    st.write("")
    
    # Chargement initial des données métiers
    df = get_dynamic_explorer()

    # =========================================================================
    # SECTION 1 : LE BUBBLE CHART (ANALYSE PAR MÉTIER)
    # =========================================================================
    st.subheader("💼 1. Cartographie Sectorielle des Professions")
    st.markdown(
        "Cette interface interactive s'inspire de la célèbre approche *Gapminder* pour cartographier le marché du travail face à l'IA. "
        "Chaque bulle représente un métier unique. La taille de la bulle est proportionnelle au volume de postes ouverts, et sa couleur "
        "indique son exposition au risque."
    )
    st.write("")
    
    # Sélecteur de niveau d'expérience
    exp_levels = ["Tous"] + sorted(list(df["experience_level"].unique()))
    selected_exp = st.selectbox(
        "🌍 Filtrer la cartographie par niveau d'expérience requis :", 
        exp_levels,
        help="Permet d'isoler l'impact de l'IA selon le niveau de séniorité du poste."
    )

    # Filtrage dynamique du DataFrame
    df_filtered = df if selected_exp == "Tous" else df[df["experience_level"] == selected_exp]

    # Rendu du graphique à bulles
    if not df_filtered.empty:
        fig = generate_dynamic_bubble_chart(df_filtered)
        st.plotly_chart(fig, use_container_width=True)
    
        # Métriques dynamiques
        distinct_jobs = df_filtered["job_title"].nunique()
        total_openings = int(df_filtered["job_openings"].sum())
    
        st.info(
            f"💡 La sélection actuelle affiche **{distinct_jobs} métiers uniques** "
            f"pour un volume total de **{total_openings:,}** opportunités d'emploi."
        )
    else:
        st.warning("Aucune donnée disponible pour ce niveau d'expérience.")
    
    st.write("---")

    # =========================================================================
    # SECTION 2 : LE HEATMAP (DENSITÉ MACROÉCONOMIQUE)
    # =========================================================================
    st.subheader(" 📊 2. Matrice de Densité des Risques par Pays")
    st.markdown(
        "Ce Heatmap croise les volumes de postes ouverts selon les pays et leur vulnérabilité à l'IA. "
        "Les zones chaudes (rouges) indiquent les plus fortes concentrations d'emplois sur le marché actuel."
    )
    st.write("")

    try:
        df_heatmap = get_heatmap()
        fig_heatmap = generate_risk_heatmap(df_heatmap)
        st.plotly_chart(fig_heatmap, use_container_width=True)
    except Exception as e:
        st.error(f"Erreur lors du chargement de la matrice de densité : {e}")

    st.write("---")

    # =========================================================================
    # SECTION 3 : LA CARTE CHOROPLÈTHE (MATURITÉ NUMÉRIQUE - EUROSTAT)
    # =========================================================================
    st.subheader(" 🇪🇺 3. Cartographie de la Digitalisation en Europe")
    st.markdown("Cette carte interactive présente le niveau moyen de compétences numériques et de digitalisation par pays "
        "selon les dernières données officielles d'**Eurostat**."
    )
    st.write("")

    try:
        df_map = get_eurostat_map()
        if not df_map.empty:
            fig_map = generate_eurostat_choropleth(df_map)
            st.plotly_chart(fig_map, use_container_width=True)
        else:
            st.warning("Aucune donnée géographique européenne disponible.")
    except Exception as e:
        st.error(f"Erreur lors du chargement de la carte Eurostat : {e}")