from models.database import execute_query
import pandas as pd
import sqlite3
from pathlib import Path


def get_db_connection():
    """
    Calcule dynamiquement le chemin absolu vers le dossier SQL/database.db
    peu importe d'où l'application Streamlit est lancée.
    """
    root_dir = Path(__file__).resolve().parent.parent.parent
    db_path = root_dir / "SQL" / "database.db"
    
    return sqlite3.connect(str(db_path))


def get_raw_ai_data():
    """Récupère la table globale sur l'impact de l'IA"""
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM ai_job_impact", conn)
    conn.close()
    return df

def get_raw_future_jobs():
    """Récupère la table globale sur les métiers du futur"""
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM future_jobs", conn)
    conn.close()
    return df

def get_raw_eurostat_isoc():
    """Récupère la table globale Eurostat"""
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM eurostat_isoc", conn)
    conn.close()
    return df

def get_top_risky_jobs(): #KPI 1
    return execute_query(
        "query_01_top_risky_jobs.sql"
    )

def get_risky_industries(): #KPI 2
    return execute_query(
        "query_02_risky_industries.sql"
    )

def get_salary_impact(): #KPI 5
    return execute_query(
        "query_05_salary_impact.sql"
    )

def get_upskilling(): #KPI 6
    return execute_query(
        "query_06_upskilling_jobs.sql"
    )

def get_top_digital_countries(): #KPI 7
    return execute_query(
        "query_07_top_digital_countries.sql"
    )
def get_digital_trend(): #KPI 8
    return execute_query(
        "query_08_digital_trend.sql"
    )

def get_top_future_jobs(): #KPI 3
    return execute_query(
        "query_03_top_future_jobs.sql"
    )

def get_best_future_jobs(): #KPI 4
    return execute_query(
        "query_04_best_future_jobs.sql"
    )

def get_dynamic_explorer(): #KPI 9
    return execute_query(
        "query_09_dynamic_explorer.sql"
    )

def get_heatmap(): #KPI 10
    return execute_query(
        "query_10_heatmap.sql"
    )

def get_eurostat_map(): #KPI11
    return execute_query(
        "query_11_eurostat_map.sql"
    )
