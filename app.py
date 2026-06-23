import streamlit as st

# Movie Data
movies = [
    "Inception",
    "Interstellar",
    "Avatar",
    "Titanic",
    "The Dark Knight",
    "Avengers: Endgame",
    "Joker"
]

# Recommendations
recommendations = {
    "Inception": ["Interstellar", "The Dark Knight", "Joker"],
    "Interstellar": ["Inception", "Avatar", "Titanic"],
    "Avatar": ["Titanic", "Interstellar", "Avengers: Endgame"],
    "Titanic": ["Avatar", "Interstellar", "Joker"],
    "The Dark Knight": ["Inception", "Joker", "Avengers: Endgame"],
    "Avengers: Endgame": ["Avatar", "The Dark Knight", "Interstellar"],
    "Joker": ["The Dark Knight", "Inception", "Titanic"]
}

# App Title
st.title("🎬 Movie Recommendation System")

st.write("Select a movie and get recommendations.")

# Movie Selection
selected_movie = st.selectbox(
    "Choose a Movie",
    movies
)

# Recommend Button
if st.button("Recommend"):
    st.subheader("Recommended Movies:")
    
    for movie in recommendations[selected_movie]:
        st.write("✅", movie)

st.markdown("---")
st.write("Developed using Python & Streamlit")
