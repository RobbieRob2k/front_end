import streamlit as st
import time

# Function to mimic a 30-second loading process
def simulate_loading():
    # Number of steps for the progress bar
    num_steps = 100
    # Time interval (in seconds) for each step
    step_interval = 30 / num_steps

    for i in range(num_steps + 1):
        st.progress(i)
        time.sleep(step_interval)

# Run the app
if __name__ == "__main__":
    st.title("Simulated Loading")

    # Button to start the loading process
    if st.button("Start Loading"):
        st.text("Loading in progress...")
        simulate_loading()
        st.success("Loading Complete!")
