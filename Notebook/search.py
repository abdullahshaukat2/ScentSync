from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import pickle

vectorizer = pickle.load(open("Model/tfidf_vectorizer.pkl", "rb"))
x = pickle.load(open("Model/tfidf_matrix.pkl", "rb"))
df = pickle.load(open("Model/data.pkl", "rb"))

def search(query):
    query_vec = vectorizer.transform([query])
    sim = cosine_similarity(query_vec, x).flatten()
    top_indices = sim.argsort()[-5:][::-1]
    results = df.iloc[top_indices][["Perfume", "Brand"]]
    results = df.iloc[top_indices].copy()
    results["similarity"] = sim[top_indices]
    return results[["Perfume", "Brand", "similarity"]]

bert_model = SentenceTransformer('all-MiniLM-L6-v2')
bert_embeddings = pickle.load(open("Model/bert_embeddings.pkl", "rb"))

def search_bert(query):
    query_vec = bert_model.encode([query])
    sim = cosine_similarity(query_vec,bert_embeddings).flatten()
    top_indices = sim.argsort()[-5:][::-1]
    results = df.iloc[top_indices].copy()
    results["similarity"] = sim[top_indices]
    return results[[
        "Perfume",
        "Brand",
        "similarity"]]

def search_bert_extended(query):

    query_vec = bert_model.encode([query])

    sim = cosine_similarity(
        query_vec,
        bert_embeddings
    ).flatten()

    top_indices = sim.argsort()[-50:][::-1]

    results = df.iloc[top_indices].copy()

    results["similarity"] = sim[top_indices]

    return results
