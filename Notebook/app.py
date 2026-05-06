import streamlit as st

from search import search, search_bert
from dupe_detector import get_dupes

st.title("ScentSync")
st.subheader("AI-Powered Fragrance Recommendation Engine")

query = st.text_input(
    "Describe a fragrance you want:"
)

model_choice = st.selectbox(
    "Choose Model",
    ["TF-IDF", "BERT"]
)

if query:

    # Select model
    if model_choice == "TF-IDF":
        results = search(query)

    else:
        results = search_bert(query)

    st.subheader("Top Recommendations")

    st.dataframe(results)

    # Dupes
    dupes = get_dupes(query)

    st.subheader("Affordable Alternatives")

    st.dataframe(dupes)