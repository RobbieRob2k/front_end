import streamlit as st

# Set the title of the web page
st.title("This is a Test Website")

# Create a subheader
st.subheader("This is My Selection")

# Create a list to store select boxes
select_boxes = []

# Function to create a new select box
def create_select_box():
    if len(select_boxes) < 10:
        new_select_box = st.selectbox(f"Select Option {len(select_boxes) + 1}", ["Option A", "Option B", "Option C"])
        select_boxes.append(new_select_box)
    else:
        st.warning("You've reached the maximum limit of 10 select boxes.")

# Create three initial select boxes
for _ in range(3):
    create_select_box()

# Button to add a new select box
if st.button("Add Another Select Box"):
    create_select_box()

# Display the select boxes
for i, select_box in enumerate(select_boxes):
    st.write(f"Option {i + 1}: {select_box}")
