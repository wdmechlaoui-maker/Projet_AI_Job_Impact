# Fichier : StreamlitApp/views/home_view.py
import streamlit as st
import pandas as pd
from utils.ui import load_global_css

def show():
    # ==========================================
    # EN-TÊTE PRINCIPAL
    # ==========================================
    st.title(" AI Job Impact Dashboard")
    st.subheader(" ✨ Plateforme décisionnelle d'analyse prospective du marché de l'emploi face à l'IA")
    
    st.markdown(" ") # Respiration

    # ==========================================
    # SECTION 1 : LES MÉTRIQUES CLÉS DU PROJET
    # ==========================================
    # On passe sur 4 colonnes pour intégrer la volumétrie de ta BDD
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.metric(label="🎯 Analyses & KPI", value="11", delta="Prêts")
    with m2:
        st.metric(label="📊 Sources de Données", value="3", delta="Eurostat + IA")
    with m3:
        st.metric(label="🌍 Pays Couverts", value="35+", delta="Europe")
    with m4:
        st.metric(label="🗄️ Traitement BDD", value="SQLite", delta="Local MVC")

    st.markdown("---")

    # ==========================================
    # SECTION 2 : CARTOGRAPHIE DU DASHBOARD (Présentation en colonnes)
    # ==========================================
    st.subheader(" Exploration du Tableau de Bord")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### ⚡ Impact & Risques")
        st.write("""
        * Métiers les plus exposés
        * Secteurs à risque
        * Évolution des salaires
        """)
        
    with col2:
        st.markdown("#### 🇪🇺 Contexte Européen")
        st.write("""
        * Classement Eurostat
        * Maturité numérique
        * Tendances temporelles
        """)
        
    with col3:
        st.markdown("#### 🚀 Opportunités")
        st.write("""
        * Métiers d'avenir
        * Taux d'Upskilling requis
        * Arbitrages Carrières
        """)

    st.markdown("---")

    # ==========================================
    # SECTION 3 : STACK TECHNIQUE 
    # ==========================================
    st.subheader("🛠️ Architecture & Technologies")
    
    # Au lieu d'utiliser des métriques avec des coches (un peu lourdes),
    # on utilise des petits badges textuels en ligne pour un rendu très sobre
    st.markdown("""
    `Python 3.13`  •  `SQL (SQLite)`  •  `Pandas`  •  `Plotly (Interactif)`  •  `Streamlit (MVC)`
    """)

    st.markdown("---")

    # ==========================================
    # SECTION 4 : MÉTHODOLOGIE 
    # ==========================================

    with st.expander("📂 Sources des données & Méthodologie"):
        st.markdown("""
        **Origine des 3 jeux de données exploités :**
        
        1. **AI Impact on Job Sector** (via [Kaggle](https://www.kaggle.com/datasets/sumeakash/ai-impact-on-job-sector)) : 
        Analyse des volumes d'ouvertures de postes, de l'évolution des industries et des exigences d'adaptation du marché.
        
        2. **AI Job Risk & Salary Dataset 2015-2035** (via [Kaggle](https://www.kaggle.com/datasets/shree0910/ai-job-risk-and-salary-dataset-20152035)) : 
        Projections et modélisations des scores de risque IA croisés avec l'historique et le futur des grilles salariales sur 20 ans.
        
        3. **Indicateurs de Compétences Numériques** (via [Eurostat - Table `isoc_sk_dskl_i21`](https://ec.europa.eu/eurostat/databrowser/view/isoc_sk_dskl_i21__custom_21070744/default/bar?lang=en)) : 
        Statistiques officielles de l'Union Européenne mesurant le niveau global et l'évolution de la maturité numérique par pays.
        
        ---
        *L'ensemble de ces bases a été nettoyé, standardisé, harmonisé, modélisé et centralisé dans notre base de données locale SQLite.*
        """)

    # Guide de navigation final discret
    st.info("👋 **Prêt à explorer ?** Utilisez le menu latéral à gauche pour naviguer entre les différentes analyses.")

    st.markdown("---")

    with st.expander("🔍 Explorer et Télécharger les Jeux de Données (Open Data)"):
        st.write("Accédez aux tables brutes stockées dans la base SQLite ayant servi à alimenter les analyses du dashboard.")
        
        # 1. Import des fonctions du contrôleur
        from controllers.ai_controller import (get_raw_ai_data, get_raw_future_jobs, get_raw_eurostat_isoc)
        
        # 2. Création des onglets pour chaque table
        tab_ai, tab_future, tab_eurostat = st.tabs([
            "💼 Impact IA", 
            "🚀 Métiers du Futur", 
            "🇪🇺 Compétences Eurostat"
        ])
        
        # --- ONGLET 1 : IMPACT IA ---
        with tab_ai:
            try:
                df_ai = get_raw_ai_data()
                st.markdown(f"**Table :** `ai_job_impact` | **Volume :** {len(df_ai):,} lignes, {len(df_ai.columns)} colonnes".replace(",", " "))
                st.dataframe(df_ai.head(10), use_container_width=True)
                
                st.download_button(
                    label="📥 Télécharger les données Impact IA (CSV)",
                    data=df_ai.to_csv(index=False).encode('utf-8'),
                    file_name="raw_ai_job_impact.csv",
                    mime="text/csv",
                    key="btn_dl_ai"
                )
            except Exception as e:
                st.error(f"Impossible de charger la table Impact IA : {e}")

        # --- ONGLET 2 : MÉTIERS DU FUTUR ---
        with tab_future:
            try:
                df_future = get_raw_future_jobs()
                st.markdown(f"**Table :** `future_jobs` | **Volume :** {len(df_future):,} lignes, {len(df_future.columns)} colonnes".replace(",", " "))
                st.dataframe(df_future.head(10), use_container_width=True)
                
                st.download_button(
                    label="📥 Télécharger les données Métiers du Futur (CSV)",
                    data=df_future.to_csv(index=False).encode('utf-8'),
                    file_name="raw_future_jobs.csv",
                    mime="text/csv",
                    key="btn_dl_future"
                )
            except Exception as e:
                st.error(f"Impossible de charger la table Métiers du Futur : {e}")

        # --- ONGLET 3 : EUROSTAT ---
        with tab_eurostat:
            try:
                df_isoc = get_raw_eurostat_isoc()
                st.markdown(f"**Table :** `eurostat_isoc` | **Volume :** {len(df_isoc):,} lignes, {len(df_isoc.columns)} colonnes".replace(",", " "))
                st.dataframe(df_isoc.head(10), use_container_width=True)
                
                st.download_button(
                    label="📥 Télécharger les données Eurostat (CSV)",
                    data=df_isoc.to_csv(index=False).encode('utf-8'),
                    file_name="raw_eurostat_isoc.csv",
                    mime="text/csv",
                    key="btn_dl_isoc"
                )
            except Exception as e:
                st.error(f"Impossible de charger la table Eurostat : {e}")
    