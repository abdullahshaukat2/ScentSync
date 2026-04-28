from sklearn.metrics.pairwise import cosine_similarity

import pickle

vectorizer = pickle.load(open("Model/tfidf_vectorizer.pkl", "rb"))
x = pickle.load(open("Model/tfidf_matrix.pkl", "rb"))
df = pickle.load(open("Model/data.pkl", "rb"))

def search(query):
    query_vec = vectorizer.transform([query])
    sim = cosine_similarity(query_vec, x).flatten()
    top_indices = sim.argsort()[-5:][::-1]
    results = df.iloc[top_indices][["Perfume", "Brand"]]
    return results

