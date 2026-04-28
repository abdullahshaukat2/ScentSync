from pre_processing import load_and_clean_data
from tfidf_model_build import build_tfidf_model
from search import search

df = load_and_clean_data()
build_tfidf_model(df)


print(search("vanilla sweet warm"))