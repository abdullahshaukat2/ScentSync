from sentence_transformers import SentenceTransformer
import pickle
import numpy as np

def build_bert_embeddings(df):

    model = SentenceTransformer('all-MiniLM-L6-v2')

    embeddings = model.encode(df["bert_text"].tolist(),  show_progress_bar=True)
    embeddings = np.array(embeddings)

    pickle.dump(embeddings,open("Model/bert_embeddings.pkl", "wb"))

    print("✅ BERT embeddings saved!")

