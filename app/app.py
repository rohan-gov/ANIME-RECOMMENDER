import streamlit as st
from pipeline.pipeline import AnimeRecommenderPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommenderPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter an anime title or description e.g. light hearted anime with school settings : ", "")

if st.button("Get Recommendations"):
    if query:
        with st.spinner("Fetching recommendations..."):
            try:
                recommendations = pipeline.recommendations(query)
                st.subheader("Recommended Anime:")
                st.write(recommendations)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid anime title or description.")




