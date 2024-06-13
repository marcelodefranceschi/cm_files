import streamlit as st
import os
import pandas as pd
import subprocess


st.title("Cost Management June 2024")
st.write("#### Page to download templates and upload back the Project's forecast")

Tunnels_file = "New_Pillar_Tunnels.xlsx"


with open(Tunnels_file, 'rb') as file:
    st.download_button(
            label="Download Tunnels file",
            data=file,
            file_name="Pillar based cost data sheet May-24 WD3 Rev01.xlsx",
            type="primary",
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                      )



# Define the target directory path
target_directory = r'https://lowerthamescrossing.sharepoint.com/:f:/s/Prism/EnH7fNFeuhBPufQp6FVEyzEBm78NgVJw6jP9ptKEXy1S2A?e=0PXroU'

# Create a Streamlit file uploader
uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)

# Check if files are uploaded
if uploaded_files:
    # Iterate over each uploaded file
    for file in uploaded_files:
        # Get the file name
        file_name = file.name
        # Create the full path to save the file
        file_path = os.path.join(target_directory, file_name)
        # Save the file to the target directory
        with open(file_path, "wb") as f:
            f.write(file.read())
        # Print a success message
        st.success(f"{file_name} was successfully uploaded. THANK YOU!")




#python -m streamlit run main.py