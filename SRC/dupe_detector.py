from search import search_bert_extended

dupe_brands = [
    "armaf",
    "lattafa-perfumes",
    "lattafa",
    "afnan",
    "rasasi",
    "maison-alhambra"
]

def get_dupes(query):

    results = search_bert_extended(query)

    dupes = results[
        results["Brand"].str.lower().isin(dupe_brands)
    ]

    return dupes.head(5)