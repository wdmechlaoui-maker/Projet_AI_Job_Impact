# Fichier : StreamlitApp/views/conclusion_view.py
import streamlit as st

def show():
    # Import et application du style global
    from utils.ui import load_global_css
    load_global_css()
    
    st.title("🏁 Conclusions & Perspectives")
    st.markdown("---")
    
    # =========================================================================
    # 1. RÉSUMÉ RAPIDE
    # =========================================================================
    st.subheader("📝 Résumé rapide du projet")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        * **Objectif principal :** Analyser et cartographier l'impact de l'intelligence artificielle sur le marché de l'emploi mondial et évaluer la maturité des compétences numériques en Europe pour accompagner cette transition.
        * **Jeux de données utilisés :** 
            * `clean_ai_job_impact.csv` (Offres d'emploi, salaires et niveaux de risque IA)
            * `clean_future_jobs.csv` (Projections et indices de croissance des métiers)
            * `clean_isoc.csv` (Indicateurs Eurostat sur les compétences numériques des citoyens)
        """)
    with col2:
        st.markdown("""
        * **Méthodologie & Étapes majeures :** 
            1. *Prétraitement :* Nettoyage, gestion des valeurs manquantes, alignement des nomenclatures de pays et encodage des niveaux de risque.
            2. *Pipeline SQL :* Centralisation et modélisation relationnelle dans une base **SQLite** (3 tables optimisées).
            3. *Analyses :* Création d'indicateurs (KPIs), agrégations statistiques et visualisations avancées (Matrices de densité, Cartes choroplèthes).
        """)

    # =========================================================================
    # 2. PRINCIPALES DÉCOUVERTES
    # =========================================================================
    st.subheader("💡 Principales découvertes")
    
    # Affichage en 3 colonnes pour les 3 points clés
    kpi1, kpi2, kpi3 = st.columns(3)
    with kpi1:
        st.info("""
        **1. Le "Ventre Mou" en mutation**  
        Le gros du marché de l'emploi actuel (~25M de postes analysés par pays) se situe dans la catégorie **Medium Risk**. L'IA ne va pas détruire ces emplois massivement, mais va profondément redéfinir leurs tâches quotidiennes.
        """)
    with kpi2:
        st.success("""
        **2. Résilience du High-Skill**  
        Il existe une corrélation positive nette entre le niveau de salaire/compétence d'un poste et sa résilience ou sa capacité à collaborer avec l'IA (Augmentation plutôt que Substitution).
        """)
    with kpi3:
        st.warning("""
        **3. Le fossé numérique européen**  
        L'analyse des données Eurostat révèle de fortes disparités régionales. Certains pays accusent un retard critique en compétences numériques de base, ce qui freine leur capacité de transition économique.
        """)

    # =========================================================================
    # 3. LIMITES ET SOURCES D'INCERTITUDE
    # =========================================================================
    st.subheader("⚠️ Limites et sources d'incertitude")
    
    st.markdown("""
    Bien que les tendances observées soient robustes, plusieurs limites méthodologiques doivent être soulignées :
    * **Biais de représentativité :** Les données des offres d'emploi reflètent principalement le marché visible en ligne et surreprésentent parfois les secteurs technologiques ou tertiaires.
    * **Temporalité des données :** L'évolution de l'IA générative est extrêmement rapide. Un modèle ou un risque défini en 2024 peut rapidement muter en 2026.
    * **Données manquantes ou agrégées :** Les indicateurs de compétences Eurostat reposent sur des enquêtes déclaratives, ce qui peut induire des biais de perception chez les répondants.
    """)
    
    # Boîte de recommandation pour atténuer les limites
    st.markdown("🛠️ **Pistes d'atténuation :**")
    st.caption("Pour fiabiliser ces conclusions, il serait nécessaire d'intégrer des validations croisées avec des données de cabinets de recrutement réels, d'élargir l'échantillon aux PME locales et d'automatiser la mise à jour des risques par du Scraping en temps réel.")

    # =========================================================================
    # 4. RECOMMANDATIONS ET PROCHAINES ÉTAPES
    # =========================================================================
    st.subheader("🚀 Recommandations et prochaines étapes")
    
    rec_col1, rec_col2 = st.columns(2)
    
    with rec_col1:
        st.markdown("### 🎯 Recommandations Opérationnelles")
        st.markdown("""
        1. **Investir massivement dans l'Upskilling :** Plutôt que de craindre le remplacement, les décideurs doivent former les collaborateurs actuels (le segment *Medium Risk*) à l'utilisation des outils IA.
        2. **Cibler les politiques publiques :** Utiliser la carte interactive Eurostat pour orienter les budgets d'aide numérique vers les régions et pays affichant les scores de compétences les plus faibles.
        3. **Valoriser les compétences humaines :** Accentuer la formation sur les *soft skills* (pensée critique, management, créativité) qui restent ancrées dans la zone *Low Risk*.
        """)
        
    with rec_col2:
        st.markdown("### 💻 Prochaines étapes techniques")
        st.markdown("""
        * **Modélisation prédictive (Machine Learning) :** Intégrer un modèle de classification (Scikit-Learn) pour prédire automatiquement le niveau de risque d'un métier à partir de sa description textuelle (NLP).
        * **Monitoring et pipeline automatisé :** Mettre en place un outil d'orchestration (comme Airflow) pour mettre à jour la base SQLite automatiquement à chaque publication de nouvelles données Eurostat.
        * **Déploiement Cloud :** Déployer l'application sur *Streamlit Community Cloud* ou *Hugging Face Spaces* pour la rendre accessible publiquement aux décideurs.
        """)

    # Petit message de fin stylé
    st.markdown("---")
    st.markdown("<div style='text-align: center; font-style: italic; color: #64748B;'>Fin de la présentation du projet - AI Job Impact Dashboard • 2026</div>", unsafe_allow_html=True)