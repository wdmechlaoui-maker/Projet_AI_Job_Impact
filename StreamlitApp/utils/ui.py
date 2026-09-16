import streamlit as st
import os

def load_global_css():
    """
    Charge le fichier CSS centralisé pour l'appliquer à la page Streamlit en cours.
    """
    css_path = os.path.join("StreamlitApp", "assets", "style.css")
    
    # Sécurité si le chemin varie selon l'exécution
    if not os.path.exists(css_path):
        css_path = os.path.join("assets", "style.css")
        
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)