import sqlite3
import os

# Répertoire du fichier database.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Remonter vers StreamlitApp puis ProjetVersion1
PROJECT_ROOT = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..")
)

# Chemin vers la base SQLite
DB_PATH = os.path.join(
    PROJECT_ROOT,
    "SQL",
    "database.db"
)

def get_connection():
    """
    Retourne une connexion SQLite.
    """
    return sqlite3.connect(DB_PATH)

def load_query(filename):
    """
    Charge une requête SQL depuis le dossier Queries.
    """

    query_path = os.path.join(
        PROJECT_ROOT,
        "SQL",
        filename
    )

    with open(query_path, "r", encoding="utf-8") as f:
        return f.read()
    
import pandas as pd

def execute_query(filename):
    """
    Exécute une requête SQL stockée dans un fichier
    et retourne un DataFrame.
    """

    conn = get_connection()

    try:
        query = load_query(filename)
        df = pd.read_sql(query, conn)
        return df

    finally:
        conn.close()

#Test of connexion
# if __name__ == "__main__":
#     df = execute_query("query_01_top_risky_jobs.sql")
#     print(df.head())    