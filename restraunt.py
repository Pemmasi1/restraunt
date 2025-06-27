import streamlit as st
from langchain_helper import generate_restaurant_idea

st.set_page_config(page_title="Restaurant Generator", page_icon="🍽️")

st.title("🍽️ Restaurant Name & Menu Generator")
st.markdown("Create a unique restaurant concept powered by AI.")

# Sidebar for input
st.sidebar.header("Choose Cuisine")
cuisine = st.sidebar.selectbox(
    "Select a cuisine:",
    [
        "Italian", "Indian", "Mexican", "Chinese", "Japanese", 
        "Thai", "French", "American", "Mediterranean", "Korean"
    ]
)

# Main page content
if st.button("Generate"):
    with st.spinner("Generating ideas..."):
        result = generate_restaurant_idea(cuisine)
        st.markdown("### 🍴 Suggested Restaurant Concept")
        st.text(result)
