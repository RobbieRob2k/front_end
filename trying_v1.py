import streamlit as st
import time

# Function to simulate loading UI
def load_ui():
    for i in range(101):
        time.sleep(0.02)  # Simulate a delay
        st.progress(i)
    st.text("UI Loaded")

# Function to simulate API request
def make_api_request():
    for i in range(101):
        time.sleep(0.02)  # Simulate a delay
        st.progress(i)
    st.text("API Request Completed")

# Function to simulate model processing
def process_data_with_model():
    for i in range(101):
        time.sleep(0.02)  # Simulate a delay
        st.progress(i)
    st.text("Model Processing Completed")

# Run the app
if __name__ == "__main__":
    st.title("Loading Progress Example")

    # Button to start the process
    if st.button("Start Process"):
        st.text("Loading UI...")
        load_ui()

        st.text("Making API Request...")
        make_api_request()

        st.text("Processing Data with Model...")
        process_data_with_model()

        st.success("All Processes Completed!")
