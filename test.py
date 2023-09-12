import streamlit as st
import requests

# Placeholder API endpoint
# api_url = "https://jsonplaceholder.typicode.com/posts"

# Read the list of movies from the text file
with open("movies2.txt", "r", encoding="cp1252") as file:
    movies = [line.strip() for line in file]

# Streamlit UI
st.title("Your Personalized Movie Recommendations")

# Create six empty lists to store the selected movies
selected_movies = [st.selectbox(f"Select Movie {i+1}", movies) for i in range(6)]

"""
# Create a button to fetch data from the API
if st.button("Fetch Data from API"):
    try:
        # Make a placeholder API request to fetch data
        response = requests.get(api_url)
        data = response.json()

        # Display the fetched data
        st.subheader("API Data:")
        for item in data:
            st.write(f"Title: {item['title']}")
            st.write(f"Body: {item['body']}")
            st.write("---")

    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
"""
# Run the app
if __name__ == "__main__":
    st.set_page_config(page_title="Your Personalized Movie Recommendations")
    st.write("Instructions: Select your favorite movies, and click 'Fetch Data from API' to view API data.")
