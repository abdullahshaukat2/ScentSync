from search import search, search_bert

queries = [
    "warm cozy date night",
    "fresh aquatic summer",
    "sweet vanilla sexy",
    "date night",
    "cool gym fresh",
    "I want a perfume that is fresh and aquatic, perfect for summer days"
]

for q in queries:

    print("\nQUERY:", q)

    print("\nTF-IDF")
    print(search(q))

    print("\nBERT")
    print(search_bert(q))
