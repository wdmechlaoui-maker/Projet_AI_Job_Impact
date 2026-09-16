# Fichier : StreamlitApp/app.py
import streamlit as st
from streamlit_option_menu import option_menu

from views.home_view import show as home_show
from views.ai_impact_view import show as ai_show
from views.future_jobs_view import show as future_show
from views.explorer_view import show as explorer_show
from views.europe_view import show as europe_show
from views.conclusion_view import show as conclusion_show
from views.contact_view import show as contact_show

# IMPORT DE LA FONCTION CSS DEPUIS UTILS
from utils.ui import load_global_css

import os
import sys
from pathlib import Path

# Configuration de la page principale
st.set_page_config(
    page_title="AI Job Impact Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================================================================
# INJECTION SÉCURISÉE DU CSS GLOBAL AVANT TOUT RENDU (MÊME LA SIDEBAR)
# =========================================================================
load_global_css()

# ==========================================
# BARRE LATÉRALE DE NAVIGATION (SIDEBAR)
# ==========================================
with st.sidebar:
    # 1. Gestion et affichage de l'image locale personnalisée
    image_path = os.path.join("..","Images","dataset-cover.png")
    
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        chemin_alternatif = os.path.join("Images", "dataset-cover.png")
        if os.path.exists(chemin_alternatif):
            st.image(chemin_alternatif, use_container_width=True)
        else:
            st.markdown("<h1 style='text-align: center; margin: 0;'>🤖</h1>", unsafe_allow_html=True)
            
    st.markdown("---")

    # 2. Menu de navigation avec injection de styles CSS avancés
    selected = option_menu(
        menu_title=None, 
        options=[
            "Accueil",
            "Impact IA",
            "Métiers du futur",
            "Europe numérique",
            "Explorateur",
            "Conclusions",
            "Contact & Avis"
        ],
        icons=[
            "house",
            "robot",
            "rocket-takeoff",
            "globe-europe-africa",
            "compass",
            "clipboard-data",
            "envelope"
        ],
        default_index=0,
        styles={
            "container": {
                "padding": "0!important", 
                "background-color": "transparent"
            },
            "icon": {
                "color": "#64748B", 
                "font-size": "16px"
            }, 
            "nav-link": {
                "font-size": "14px", 
                "text-align": "left", 
                "margin": "4px 0px", 
                "border-radius": "8px",
                "color": "#1E293B",
                "font-family": "'Source Sans Pro', sans-serif"
            },
            "nav-link-selected": {
                "background-color": "#2b5c8f", 
                "color": "white",
                "font-weight": "600"
            }
        }
    )

    st.markdown("---")
    
    # 3. Petit pied de page discret dans la sidebar
    st.markdown("""
    <div style='text-align: center; color: #94A3B8; font-size: 11px;'>
        Projet Data Analytics • 2026
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# LOGIQUE DE ROUTAGE DES VUES
# ==========================================
if selected == "Accueil":
    home_show()

elif selected == "Impact IA":
    ai_show()

elif selected == "Métiers du futur":
    future_show()

elif selected == "Europe numérique":
    europe_show()

elif selected == "Explorateur":  
    explorer_show()

elif selected == "Conclusions":
    conclusion_show()
    
elif selected == "Contact & Avis":
    contact_show()