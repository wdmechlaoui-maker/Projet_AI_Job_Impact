import sqlite3
import pandas as pd
# Création (ou ouverture) du fichier .db
conn = sqlite3.connect("database.db")

# Toujours créer un curseur
cursor = conn.cursor()

print("Base SQLite créée !")

from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

df_ai = pd.read_csv(base_dir / "Data" / "clean_ai_job_impact.csv")
df_future = pd.read_csv(base_dir / "Data" / "clean_future_jobs.csv")
df_isoc = pd.read_csv(base_dir / "Data" / "clean_isoc.csv")

#print("df_ai :", df_ai.shape)
#print("df_future :", df_future.shape)
#print("df_isoc :", df_isoc.shape)
#print(df_ai.head())

df_ai.to_sql("ai_job_impact", conn, if_exists="replace", index=False)
df_future.to_sql("future_jobs", conn, if_exists="replace", index=False)
df_isoc.to_sql("eurostat_isoc", conn, if_exists="replace", index=False)

conn.commit()
print("Tables ajoutées à la base SQLite !")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())


#Fermer la connexion
conn.close()