# Fichier : StreamlitApp/views/europe_view.py
import streamlit as st
from utils.ui import load_global_css
import os
import sys
from pathlib import Path

# Détermination du chemin vers la racine réelle du projet (ProjetVersion1)
root_path = Path(__file__).resolve().parent.parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))
    

# Import des fonctions du Controller
from controllers.ai_controller import (
    get_top_digital_countries,
    get_digital_trend
)


# Importations magiques des fonctions graphiques modulaires
from views.Visualisations.viz_07_digital_countries import generate_digital_countries_chart
from views.Visualisations.viz_08_digital_trend import generate_digital_trend_chart

def show():
    
    st.title("🇪🇺 Analyse du Niveau de Digitalisation en Europe")
    
    st.markdown("""
    Cette page examine la maturité numérique des pays européens (données Eurostat) 
    afin de comprendre le contexte macroéconomique face à l'adoption de l'IA.
    """)
    
    # Récupération des données
    df_countries = get_top_digital_countries()
    df_trend = get_digital_trend()
    
    # =========================================================================================
    # KPI 7 : Top 10 des pays avancés
    # =========================================================================================
    st.markdown("---")
    st.subheader("🏆 Top 10 des pays les plus avancés numériquement")
    
    fig_countries = generate_digital_countries_chart(df_countries)
    st.plotly_chart(fig_countries, use_container_width=True)
    
    st.info("""
    **Zoom d'analyse :** L'axe des abscisses démarre volontairement à 60% pour mettre en relief 
    les écarts serrés entre les nations leaders. On observe une forte maturité des pays d'Europe du Nord.
    """)
    
    # =========================================================================================
    # KPI 8 : Tendance temporelle globale
    # =========================================================================================
    st.markdown("---")
    st.subheader("📈 Évolution du niveau de digitalisation global")
    
    fig_trend = generate_digital_trend_chart(df_trend)
    st.plotly_chart(fig_trend, use_container_width=True)
    
    st.info("""
    **Enseignement historique :** La courbe met en évidence la trajectoire et le rythme 
    de la transition numérique globale en Europe au fil des années.
    """)