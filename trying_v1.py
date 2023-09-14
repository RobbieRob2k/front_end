import streamlit as st

# Set the title of the web page
st.title("This is a Test Website")

# Create a subheader
st.subheader("This is My Selection")

# Create three select boxes
selected_option_1 = st.selectbox("Select Option 1", ["Option 1", "Option 2", "Option 3"])
selected_option_2 = st.selectbox("Select Option 2", ["Option A", "Option B", "Option C"])
selected_option_3 = st.selectbox("Select Option 3", ["Choice X", "Choice Y", "Choice Z"])
