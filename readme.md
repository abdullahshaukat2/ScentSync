# ScentSync 🌸

ScentSync is an AI-powered fragrance recommendation and dupe discovery system built using NLP, semantic search, and transformer embeddings. The project analyzes over 24,000+ fragrances from the Fragrantica dataset and recommends similar fragrances based on scent notes, accords, and contextual fragrance descriptions.

Users can search using natural-language queries such as:

- "warm cozy date night fragrance"
- "fresh aquatic summer scent"
- "cool gym fragrance"

ScentSync also identifies affordable fragrance alternatives ("dupes") from clone-house brands such as Armaf, Lattafa, Afnan, and Maison Alhambra.

---

# Features

- AI-powered fragrance recommendations
- Semantic fragrance search
- TF-IDF recommendation pipeline
- Sentence-BERT semantic embeddings
- Affordable dupe detection system
- Cosine similarity retrieval
- Streamlit web application
- Top-K recommendation retrieval
- NLP preprocessing and feature engineering

---

# Dataset

Dataset Source:
- Fragrantica Kaggle Dataset

Dataset Size:
- 24,000+ fragrances

Dataset includes:
- fragrance names
- brands
- top notes
- middle notes
- base notes
- accords
- fragrance metadata

---

# Tech Stack

## Languages & Libraries
- Python
- Pandas
- NumPy
- Scikit-learn
- Sentence-Transformers
- Streamlit
- Pickle

## NLP / ML Techniques
- TF-IDF Vectorization
- Sentence-BERT Embeddings
- Cosine Similarity
- Semantic Search
- Recommendation Systems

---

# Project Architecture

```text
User Query
    ↓
Preprocessing Pipeline
    ↓
TF-IDF / Sentence-BERT Embeddings
    ↓
Cosine Similarity Search
    ↓
Top-K Fragrance Recommendations
    ↓
Affordable Dupe Detection