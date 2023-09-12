import streamlit as st
import requests

# API endpoints
recommendations_endpoint = "https://api.example.com/recommendations"  # Replace with the actual recommendations endpoint
movie_list_endpoint = "https://api.example.com/movies"  # Replace with the actual movie list endpoint

# Streamlit UI
st.title("Your Personalized Movie Recommendations")

# Create six empty lists to store the selected movies
selected_movies = [st.selectbox(f"Select Movie {i+1}", []) for i in range(6)]

# Function to get movie recommendations from the API
def get_recommendations(selected_movies):
    try:
        # Create a JSON payload with selected movies
        payload = {"movies": selected_movies}

        # Make a POST request to the recommendations endpoint
        response = requests.post(recommendations_endpoint, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            recommendations = response.json()
            return recommendations
        else:
            st.error(f"Error fetching recommendations: {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        st.error(f"API request error: {e}")
        return []

# Function to get the movie list from the API
def get_movie_list():
    try:
        # Make a GET request to the movie list endpoint
        response = requests.get(movie_list_endpoint)

        # Check if the request was successful
        if response.status_code == 200:
            movie_list = response.json()
            return movie_list
        else:
            st.error(f"Error fetching movie list: {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        st.error(f"API request error: {e}")
        return []

# Create a button to fetch movie recommendations
if st.button("Get Recommendations"):
    recommendations = get_recommendations(selected_movies)

    # Display recommendations to the user
    st.subheader("Recommended Movies:")
    for i, movie in enumerate(recommendations):
        st.write(f"{i+1}. {movie}")

# Fetch and populate the movie list
movie_list = get_movie_list()
if movie_list:
    selected_movies = [st.selectbox(f"Select Movie {i+1}", movie_list) for i in range(6)]

# Run the app
if __name__ == "__main__":
    st.set_page_config(page_title="Your Personalized Movie Recommendations")
    st.write("Instructions: Select your favorite movies, and click 'Get Recommendations' to view movie recommendations.")
