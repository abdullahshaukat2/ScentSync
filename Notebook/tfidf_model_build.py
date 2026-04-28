from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def build_tfidf_model(df):
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(df["combined"])

    pickle.dump(vectorizer, open("Model/tfidf_vectorizer.pkl", "wb"))
    pickle.dump(x, open("Model/tfidf_matrix.pkl", "wb"))
    pickle.dump(df, open("Model/data.pkl", "wb")) 
    