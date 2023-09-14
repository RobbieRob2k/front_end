import streamlit as st
import requests
import time

# Function to simulate a 30-second loading process
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

# API endpoint
recommendations_endpoint = "http://localhost:8000/predict"

# ... (Rest of your code for selecting movies)

# Button on UI to get recommendations
if st.button("Get My Movie Recommendations!"):
    # Display loading bar
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
