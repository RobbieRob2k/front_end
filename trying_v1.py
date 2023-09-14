mport streamlit as st
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
In this example, the simulate_loading function gradually updates the progress bar by looping through 100 steps over a 30-second duration. It introduces a delay between each step to create the effect of a slow loading process.

When you click the "Start Loading" button, you'll see the progress bar slowly fill over the course of 30 seconds, simulating a loading process. This approach allows you to mimic the appearance of a real loading time while actually controlling the duration programmatically.

Feel free to adjust the num_steps and step_interval variables to fine-tune the speed and duration of the progress bar as needed for your application.





