import streamlit as st
import requests
import time

# Function to mimic a 30-second loading process
def simulate_loading():
    st.write("Loading in progress...")
    progress_bar = st.progress(0)

    # Number of steps for the progress bar
    num_steps = 100
    # Time interval (in seconds) for each step
    step_interval = 30 / num_steps

    for i in range(num_steps + 1):
        progress_bar.progress(i)
        time.sleep(step_interval)

    st.success("Loading Complete!")

st.title("Get Your AI-Powered Movie Recommendations 🎬🤖🍿", anchor="center")

# API endpoint 
recommendations_endpoint = "http://localhost:8000/predict"

# reads list of movies saved in this text file, needs to be updated once new movies added; note: ASIN formatting
with open("movies2.txt", "r", encoding="cp1252") as file:
    movies_list = [line.strip() for line in file]

st.subheader("Select Your Favorite Movies:")
selected_movies_best = [st.selectbox(f"Select Favorite Movie {i+1}", movies_list, key=f"best_movie_{i}") for i in range(5)]

st.subheader("Select Your Least Favorite Movies:")
selected_movies_least_liked = [st.selectbox(f"Select Least Favorite Movie {i+1}", movies_list, key=f"least_liked_movie_{i}") for i in range(5)]

# combining most liked and disliked into single list for API
selected_movies = selected_movies_best + selected_movies_least_liked

# button on UI to get recommendations
# need to add genres to st.button once we can load them
if st.button("Get My Movie Recommendations!"):
    # Display loading bar while fetching recommendations
    simulate_loading()

    # Once loading is complete, fetch recommendations
    recommendations = get_recommendations_and_genres(selected_movies_best, selected_movies_least_liked)

    if recommendations:
        st.subheader("Your Top 10 Recommended Movies:")
        for i, movie in enumerate(recommendations):
            st.write(f"{i+1}. {movie}")
    else:
        st.info("No recommendations available based on your selections.")

    # Display top genres
    # st.subheader("Top Genres Based on Your Selections:")
    # for i, genre in enumerate(top_genres):
    #    st.write(f"{i+1}. {genre}")

if __name__ == "__main__":
    st.set_page_config(page_title="Your Personalized Movie Recommendations")
    st.write("Instructions: Select your top 5 favorite and top 5 least liked movies, and click 'Get Recommendations' to view movie recommendations and top genres.")
