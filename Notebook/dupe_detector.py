
dupe_brands = [
    "armaf",
    "lattafa-perfumes",
    "lattafa",
    "afnan",
    "rasasi",
    "maison-alhambra",
    "al-haramain",
    "fragrance-world"]

def get_dupes(results):
    dupes = results[results["Brand"].str.lower().isin(dupe_brands)]
    return dupes
