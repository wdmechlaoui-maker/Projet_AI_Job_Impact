import pandas as pd
import numpy as np

# Chargement des fichiers
df_ai = pd.read_csv("Data/ai_job_impact.csv")
df_future_jobs = pd.read_csv("Data/Future of Jobs AI.csv")
df_isoc = pd.read_excel("Data/estat_isoc.xlsx")
# Nettoyage des noms de colonnes
def clean_columns(df):
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("\\", "_")
    )
    return df

df_ai = clean_columns(df_ai)
df_future_jobs = clean_columns(df_future_jobs)
df_isoc = clean_columns(df_isoc)


# NETTOYAGE df_ai--------------------------------------------------------
# Harmonisation : niveaux d’éducation
education_mapping = {
    "high school": "high_school",
    "bachelor": "bachelor",
    "master": "master",
    "phd": "phd",
    "doctorate": "phd"
}

df_ai["education_level_std"] = df_ai["education_level"].str.lower().map(education_mapping)
df_future_jobs["education_level_std"] = df_future_jobs["education_level"].str.lower().map(education_mapping)

# Harmonisation : niveau d’expérience
def map_experience(years):
    if years < 3:
        return "junior"
    elif years < 10:
        return "mid_level"
    else:
        return "senior"

df_ai["experience_level_std"] = df_ai["years_experience"].apply(map_experience)


# Nettoyage colonne job_role dans df_ai
df_ai["job_role_std"] = (
    df_ai["job_role"]
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
)

# Harmonisation industries (Dataset 1 ↔ Dataset 3)
industry_mapping = {
    "Technology": "ICT",
    "Information Technology": "ICT",
    "Healthcare": "HEALTH",
    "Finance": "FIN",
    "Manufacturing": "MAN",
    "Retail": "RET",
    "Education": "EDU",
    "IT":"ICT",
    "Marketing":"MRKT"
}

df_ai["industry_std"] = df_ai["industry"].map(industry_mapping)
# Création d’une échelle commune de risque IA
risk_mapping = {
    "low": 1,
    "medium": 2,
    "high": 3
}


df_ai["ai_risk_score_std"] = df_ai["automation_risk"].str.lower().map(risk_mapping)

# NETTOYAGE df_future_jobs--------------------------------------------------------
# Nettoyage colonne job_title dans df_future_jobs
df_future_jobs["job_title_std"] = (
    df_future_jobs["job_title"]
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
)

df_future_jobs["primary_skill_std"] = (
    df_future_jobs["primary_skill"].str.strip().str.lower().str.replace(" ", "_")
)
# Harmonisation  ai_risk_score_std(Dataset 1 ↔ Dataset 2)
risk_mapping_future = {
    "low risk": 1,
    "medium risk": 2,
    "high risk": 3
}

df_future_jobs["ai_risk_score_std"] = df_future_jobs["ai_risk_category"].str.lower().map(risk_mapping_future)

# Harmonisation  experience_level(Dataset 1 ↔ Dataset 2)
experience_mapping = {
    "Entry": "junior",
    "Mid": "mid_level",
    "Senior": "senior"
}

df_future_jobs["experience_level_std"] = (
    df_future_jobs["experience_level"].str.strip().map(experience_mapping)
)


# Ajout de clés techniques
df_future_jobs.insert(
    0,
    "future_job_id",
    range(1, len(df_future_jobs) + 1)
)

# Nettoyage Dataset 3 (Eurostat ISOC)

# Transformation wide -> long
df_isoc_long = df_isoc.melt(
    id_vars=["country", "geo_time_period", "ind_type", "indic_is"],
    var_name="year",
    value_name="digital_score"
)
df_isoc_long = df_isoc_long.rename(
    columns={"geo_time_period": "country_code"}
)
# Conversion des types
df_isoc_long["year"] = pd.to_numeric(
    df_isoc_long["year"],
    errors="coerce"
)

df_isoc_long["digital_score"] = (
    df_isoc_long["digital_score"]
        .astype(str)                # force string
        .str.strip()                # supprime espaces autour
        .replace({":": None, "..": None, "": None})   # remplace après strip
)

df_isoc_long["digital_score"] = pd.to_numeric(
    df_isoc_long["digital_score"], 
    errors="coerce"
)

# Domaine de compétence numérique
domain_mapping = {
    "I_DSK2_AB": "Overall Digital Skills",
    "I_DSK2_B": "Overall Digital Skills",
    "I_DSK2_BAB": "Overall Digital Skills",

    "I_DSK2_CC_AB": "Communication & Collaboration",
    "I_DSK2_CC_B": "Communication & Collaboration",
    "I_DSK2_CC_BAB": "Communication & Collaboration",

    "I_DSK2_DCC_AB": "Digital Content Creation",
    "I_DSK2_DCC_B": "Digital Content Creation",
    "I_DSK2_DCC_BAB": "Digital Content Creation",

    "I_DSK2_IL_AB": "Information & Data Literacy",
    "I_DSK2_IL_B": "Information & Data Literacy",
    "I_DSK2_IL_BAB": "Information & Data Literacy",

    "I_DSK2_SF_AB": "Safety",
    "I_DSK2_SF_B": "Safety",
    "I_DSK2_SF_BAB": "Safety",

    "I_DSK2_PS_AB": "Problem Solving",
    "I_DSK2_PS_B": "Problem Solving",
    "I_DSK2_PS_BAB": "Problem Solving",

    "I_DSK2_IC_S": "Information & Communication",

    "I_DSK2_LW": "Overall Digital Skills",
    "I_DSK2_LM": "Overall Digital Skills",
    "I_DSK2_N": "Overall Digital Skills",
    "I_DSK2_X": "Overall Digital Skills",
    "I_DSK2_NA": "Overall Digital Skills"
}

df_isoc_long["skill_domain"] = (
    df_isoc_long["indic_is"]
    .map(domain_mapping)
)

# Niveau de compétence numérique
level_mapping = {
    "I_DSK2_AB": "Above Basic",
    "I_DSK2_B": "Basic",
    "I_DSK2_BAB": "At Least Basic",

    "I_DSK2_CC_AB": "Above Basic",
    "I_DSK2_CC_B": "Basic",
    "I_DSK2_CC_BAB": "At Least Basic",

    "I_DSK2_DCC_AB": "Above Basic",
    "I_DSK2_DCC_B": "Basic",
    "I_DSK2_DCC_BAB": "At Least Basic",

    "I_DSK2_IL_AB": "Above Basic",
    "I_DSK2_IL_B": "Basic",
    "I_DSK2_IL_BAB": "At Least Basic",

    "I_DSK2_SF_AB": "Above Basic",
    "I_DSK2_SF_B": "Basic",
    "I_DSK2_SF_BAB": "At Least Basic",

    "I_DSK2_PS_AB": "Above Basic",
    "I_DSK2_PS_B": "Basic",
    "I_DSK2_PS_BAB": "At Least Basic",

    "I_DSK2_IC_S": "Specialized",

    "I_DSK2_LW": "Low",
    "I_DSK2_LM": "Limited",
    "I_DSK2_N": "Narrow",
    "I_DSK2_X": "No Skills",
    "I_DSK2_NA": "Not Assessed"
}

df_isoc_long["skill_level"] = (
    df_isoc_long["indic_is"]
    .map(level_mapping)
)


df_isoc_long=df_isoc_long.drop_duplicates()

# Ajout de clés techniques
df_isoc_long.insert(
    0,
    "isoc_id",
    range(1, len(df_isoc_long) + 1)
)

#verification des valeurs vides et espace
#df_clean1 = df_ai.replace(r'^\s*$', np.nan, regex=True)
#print(df_clean1.isna().sum().sum())

#df_clean2 = df_future_jobs.replace(r'^\s*$', np.nan, regex=True)
#print(df_clean2.isna().sum().sum())

# Sauvegarde des datasets propres
df_ai.to_csv("Data/clean_ai_job_impact.csv", index=False)
df_future_jobs.to_csv("Data/clean_future_jobs.csv", index=False)
df_isoc_long.to_csv("Data/clean_isoc.csv", index=False)

#Affichage test de conformité des données
#print(df_isoc_long.dtypes)
#print(df_future_jobs.isna().sum())
#print((df_future_jobs.isna() | (df_future_jobs.apply(lambda col: col.astype(str).str.strip() == ""))).sum())
#print((df_ai.isna() | (df_ai.apply(lambda col: col.astype(str).str.strip() == ""))).sum())
#print((df_isoc_long.isna() | (df_isoc_long.apply(lambda col: col.astype(str).str.strip() == ""))).sum())
#print(df_isoc_long.info())
#print(df_future_jobs.info())
#print(df_future_jobs["experience_level_std"].isna().sum())
#print(df_isoc_long.info())
#print(df_isoc_long["digital_score"].isna().sum())
#print(df_future_jobs.groupby("country").size())
#print(df_ai.duplicated().sum())
#print(df_future_jobs.duplicated().sum())
#print(df_isoc_long.duplicated().sum())
#print(df_isoc_long.info())
#print(df_isoc_long["skill_domain"].isna().sum())
#print(df_isoc_long["skill_level"].isna().sum())