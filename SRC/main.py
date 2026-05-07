from pre_processing import load_and_clean_data
from tfidf_model_build import build_tfidf_model
from bert_model_build import build_bert_embeddings

df = load_and_clean_data()
build_tfidf_model(df)

build_bert_embeddings(df)

print("✅ All models built and saved successfully!")
