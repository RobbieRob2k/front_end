import streamlit as st
import requests

# API endpoints
# recommendations_endpoint = "https://api.example.com/recommendations"  

# Read the list of movies from the text file
with open("movies2.txt", "r", encoding="cp1252") as file:
    movies_list = [line.strip() for line in file]

# Streamlit UI
st.title("Your Personalized Movie Recommendations")

# Create two columns for top 5 favorites and top 5 least liked movies
col1, col2 = st.beta_columns(2)

# Create selectboxes for top 5 favorites
col1.title("Top 5 Favorite Movies")
selected_movies_fav = [col1.selectbox(f"Select Movie {i+1}", movies_list) for i in range(5)]

# Create selectboxes for top 5 least liked movies
col2.title("Top 5 Least Liked Movies")
selected_movies_dislike = [col2.selectbox(f"Select Movie {i+1}", movies_list) for i in range(5)]

"""
# Function to get movie recommendations and top genres from the API
def get_recommendations_and_genres(selected_movies_fav, selected_movies_dislike):
    try:
        # Create a JSON payload with selected movies
        payload = {
            "favorite_movies": selected_movies_fav,
            "disliked_movies": selected_movies_dislike
        }

        # Make a POST request to the recommendations endpoint
        response = requests.post(recommendations_endpoint, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            recommendations = data.get("recommendations", [])
            top_genres = data.get("top_genres", [])
            return recommendations, top_genres
        else:
            st.error(f"Error fetching recommendations: {response.status_code}")
            return [], []

    except requests.exceptions.RequestException as e:
        st.error(f"API request error: {e}")
        return [], []

# Create a button to fetch movie recommendations and top genres
if st.button("Get Recommendations"):
    recommendations, top_genres = get_recommendations_and_genres(selected_movies_fav, selected_movies_dislike)

    # Display recommendations to the user
    st.subheader("Recommended Movies:")
    for i, movie in enumerate(recommendations):
        st.write(f"{i+1}. {movie}")

    # Display top genres
    st.subheader("Top Genres Based on Your Selections:")
    for i, genre in enumerate(top_genres):
        st.write(f"{i+1}. {genre}")

# Run the app
if __name__ == "__main__":
    st.set_page_config(page_title="Your Personalized Movie Recommendations")
    st.write("Instructions: Select your top 5 favorite and top 5 least liked movies, and click 'Get Recommendations' to view movie recommendations and top genres.")
"""
