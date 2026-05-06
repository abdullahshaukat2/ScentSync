import pandas as pd

def load_and_clean_data():
    df = pd.read_csv("DataSet/fra_cleaned.csv", sep=";" , encoding="latin1")
    #print(df.head())

    df = df[[
    "Perfume", "Brand", "Gender",
    "Top", "Middle", "Base",
    "mainaccord1", "mainaccord2", "mainaccord3"
    ]]

    df = df.fillna("")

    #TF-IDF 
    df["combined"] = (
    df["Top"] + ", " +
    df["Middle"] + ", " +
    df["Base"] + ", " +
    df["mainaccord1"] + ", " +
    df["mainaccord2"] + ", " +
    df["mainaccord3"]
    )

    #BERT
    df["bert_text"] = (
    "This fragrance has top notes of " + df["Top"] +
    ", middle notes of " + df["Middle"] +
    ", base notes of " + df["Base"] +
    ". Main accords include " +
    df["mainaccord1"] + ", " +
    df["mainaccord2"] + ", " +
    df["mainaccord3"] + ".")
    df["combined"] = df["combined"].str.lower().str.replace("unknown", "")

    df = df.drop_duplicates(subset=["Perfume", "Brand"])

    return df