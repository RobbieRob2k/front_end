import streamlit as st
import requests

# API endpoint
recommendations_endpoint = "http://localhost:8000/predict"

# Reads list of movies saved in this text file; needs to be updated once new movies are added
with open("movies2.txt", "r", encoding="cp1252") as file:
    movies_list = [line.strip() for line in file]

# Create lists to store selected movies
selected_movies_best = []
selected_movies_least_liked = []

# Initially, load with 3 favorite and 3 disliked movies (you can change these initial selections)
initial_best_selections = ["Movie 1 (Liked)", "Movie 2 (Liked)", "Movie 3 (Liked)"]
initial_least_liked_selections = ["Movie 1 (Disliked)", "Movie 2 (Disliked)", "Movie 3 (Disliked)"]

# Function to get movie recommendations and top genres from the API
def get_recommendations_and_genres(selected_movies_fav, selected_movies_dislike):
    try:
        # JSON payload with selected movies
        payload = {
            "liked_movies": selected_movies_fav,
            "disliked_movies": selected_movies_dislike
        }

        # Make a POST request to the recommendations endpoint
        response = requests.get(recommendations_endpoint, params=payload)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            recommendations = data.get("Suggested Movies", [])
            top_genres = data.get("Top Genres", [])
            return recommendations, top_genres
        else:
            st.error(f"Error fetching recommendations: {response.status_code}")
            return [], []

    except requests.exceptions.RequestException as e:
        st.error(f"API request error: {e}")
        return [], []

# Streamlit UI
st.title("Your Personalized Movie Recommendations")

st.subheader("Select Your Top 3 Best Movies:")
selected_movies_best = st.multiselect("Select Movies (Best)", movies_list, initial_best_selections, key="best_movies")

st.subheader("Select Your Top 3 Least Liked Movies:")
selected_movies_least_liked = st.multiselect("Select Movies (Least Liked)", movies_list, initial_least_liked_selections, key="least_liked_movies")

# Button on UI to get recommendations
if st.button("Get My Movie Recommendations!"):
    recommendations, top_genres = get_recommendations_and_genres(selected_movies_best, selected_movies_least_liked)

    if recommendations:
        st.subheader("Your Top 10 Recommended Movies:")
        for i, movie in enumerate(recommendations):
            st.write(f"{i + 1}. {movie}")
    else:
        st.info("No recommendations available based on your selections.")

    # Display top genres
    st.subheader("Top Genres Based on Your Selections:")
    for i, genre in enumerate(top_genres):
        st.write(f"{i + 1}. {genre}")
