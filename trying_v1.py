import streamlit as st

# Set the title of the web page
st.title("This is a Test Website")

# Create a subheader
st.subheader("This is My Selection")

# Create a list to store select boxes
select_boxes = []

# Create five initial select boxes
for i in range(5):
    select_boxes.append(st.selectbox(f"Select Option {i + 1}", ["Option A", "Option B", "Option C"]))

# Display the select boxes
for i, select_box in enumerate(select_boxes):
    st.write(f"Option {i + 1}: {select_box}")

# URL to the image hosted on GitHub
background_image_url = "https://github.com/RobbieRob2k/front_end/blob/main/wallpaper.jpg?raw=true"

# Add a background image
st.markdown(
    f"""
    <style>
    body {{
        background-image: url("{background_image_url}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
