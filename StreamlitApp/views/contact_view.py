# Fichier : StreamlitApp/views/contact_view.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime
from pathlib import Path

def show():
    # Import et application du style global
    from utils.ui import load_global_css
    load_global_css()
    
    st.title("📬 Contact & Boîte aux lettres")
    st.markdown("### Votre avis nous intéresse !")
    st.write("Une suggestion ? Un bug constaté ? Laissez-nous un message pour nous aider à améliorer ce dashboard.")
    
    # 1. Création du formulaire Streamlit
    with st.form(key="contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Nom / Prénom", placeholder="Optionnel")
        with col2:
            email = st.text_input("Adresse Email", placeholder="Pour vous recontacter (Optionnel)")
            
        subject = st.selectbox(
            "Objet de votre message",
            ["Suggestion d'amélioration", "Signalement de bug", "Avis général", "Autre"]
        )
        
        message = st.text_area("Votre message *", placeholder="Écrivez votre message ici...", height=150)
        
        # Bouton de soumission
        submit_button = st.form_submit_button(label="🚀 Envoyer le message")
        
    # 2. Logique d'enregistrement au clic sur le bouton
    if submit_button:
        if not message.strip():
            st.error("Le champ 'Message' est obligatoire.")
        else:
            # Calcul du chemin vers le dossier Data
            root_dir = Path(__file__).resolve().parent.parent.parent
            feedback_file = root_dir / "Data" / "user_feedback.csv"
            
            # Préparation de la nouvelle ligne
            new_data = {
                "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "Nom": [name if name else "Anonyme"],
                "Email": [email if email else "Non renseigné"],
                "Objet": [subject],
                "Message": [message]
            }
            new_df = pd.DataFrame(new_data)
            
            try:
                # Si le fichier existe déjà, on ajoute la ligne à la suite (append)
                if feedback_file.exists():
                    new_df.to_csv(feedback_file, mode='a', header=False, index=False, encoding='utf-8')
                else:
                    # Sinon on le crée avec les entêtes
                    new_df.to_csv(feedback_file, index=False, encoding='utf-8')
                    
                st.success("🎉 Merci ! Votre message a bien été enregistré avec succès.")
                st.balloons() # Petite animation festive
                
            except Exception as e:
                st.error(f"Une erreur est survenue lors de l'enregistrement : {e}")