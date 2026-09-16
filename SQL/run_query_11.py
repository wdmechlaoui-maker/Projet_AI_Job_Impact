import os
import sqlite3
import pandas as pd
# Création (ou ouverture) du fichier .db
conn = sqlite3.connect("SQL/database.db")

# Toujours créer un curseur
cursor = conn.cursor()
#-----------Exécution Query8----------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(script_dir, "query_11_eurostat_map.sql")
with open(sql_path, "r", encoding="utf-8") as f:
    query = f.read()

# Résultat dans un DataFrame
df = pd.read_sql(query, conn)
print ("query_11_eurostat_map")
print(df)