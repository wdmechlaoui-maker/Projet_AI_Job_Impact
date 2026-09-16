# Fichier : StreamlitApp/views/future_jobs_view.py
import streamlit as st
from utils.ui import load_global_css
import os
import sys
from pathlib import Path

# Détermination du chemin vers la racine réelle du projet (ProjetVersion1)
root_path = Path(__file__).resolve().parent.parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))
    
# Imports du Controller (À adapter selon les vrais noms de tes fonctions)
from controllers.ai_controller import (
    get_top_future_jobs,
    get_best_future_jobs
)

# Imports de tes fonctions graphiques modulaires
from views.Visualisations.viz_03_future_jobs import generate_future_jobs_chart
from views.Visualisations.viz_04_promising_jobs import generate_promising_jobs_chart


def show():
    st.title("🚀 Métiers d'Avenir et Opportunités de Carrière")
    
    st.markdown("""
    Découvrez les professions qui affichent la plus forte croissance de demande sur le marché 
    et celles qui offrent les meilleurs compromis entre **rémunération attractive** et **protection face à l'automatisation**.
    """)
    
    # Récupération des données dynamiques
    df_future = get_top_future_jobs()
    df_promising = get_best_future_jobs()

    # =========================================================================================
    # KPI 3 : Top Future Jobs (Croissance de la demande)
    # =========================================================================================
    st.markdown("---")
    st.subheader("📈 Top 10 des métiers à forte croissance de demande")
    
    fig_future = generate_future_jobs_chart(df_future)
    st.plotly_chart(fig_future, use_container_width=True)
    
    st.info("""
    **Analyse :** Ce classement met en avant les rôles dont la création de postes s'accélère. 
    Les profils techniques liés à l'infrastructure IA et à la transition écologique y occupent souvent une place majeure.
    """)
    
    # =========================================================================================
    # KPI 4 : Best Future Jobs (Arbitrage Salaire / Risque)
    # =========================================================================================
    st.markdown("---")
    st.subheader("💎 Cartographie des métiers les plus prometteurs")
    
    fig_promising = generate_promising_jobs_chart(df_promising)
    st.plotly_chart(fig_promising, use_container_width=True)
    
    st.info("""
    **Guide de lecture :** Les métiers situés en **haut à gauche** représentent les opportunités idéales : 
    des salaires élevés associés à une faible exposition au risque de remplacement par l'IA (rôles à forte valeur humaine ou décisionnelle).
    """)
   