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
selected_movies_best = ["Movie 1 (Liked)", "Movie 2 (Liked)", "Movie 3 (Liked)"]
selected_movies_least_liked = ["Movie 1 (Disliked)", "Movie 2 (Disliked)", "Movie 3 (Disliked)"]

st.subheader("Select Your Top 3 Best Movies:")
for i, movie in enumerate(selected_movies_best):
    st.selectbox(f"Select Movie (Best) {i + 1}", movies_list, key=f"best_movie_{i}", index=movies_list.index(movie))

st.subheader("Select Your Top 3 Least Liked Movies:")
for i, movie in enumerate(selected_movies_least_liked):
    st.selectbox(f"Select Movie (Least Liked) {i + 1}", movies_list, key=f"least_liked_movie_{i}", index=movies_list.index(movie))

# Function to receive movie recommendations and top genres from API
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

# Button to add a new select box for liked movies
if len(selected_movies_best) < 10 and st.button("Add a Liked Movie"):
    selected_movies_best.append(movies_list[0])

# Button to add a new select box for least liked movies
if len(selected_movies_least_liked) < 10 and st.button("Add a Least Liked Movie"):
    selected_movies_least_liked.append(movies_list[0])

if __name__ == "__main__":
    st.set_page_config(page_title="Your Personalized Movie Recommendations")
    st.write("Instructions: Initially select your top 3 favorite and top 3 least liked movies. You can then click 'Add a Liked Movie' or 'Add a Least Liked Movie' to dynamically add up to a total of 10 movies for each category. Finally, click 'Get My Movie Recommendations!' to view movie recommendations and top genres.")
