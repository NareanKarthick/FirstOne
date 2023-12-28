import streamlit as st
import subprocess
import os
def save_uploaded_file(uploaded_file, save_path):
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
def main():
    st.subheader("Upload your files here")
    # File uploaders
    hotel = st.file_uploader("Amenities and Facilities", type=["pdf", "txt", "docx", "csv"])
    # Location = st.file_uploader("Location and Local Attractions", type=["pdf", "txt", "docx", "csv"])
    # Rooms = st.file_uploader("Rooms and Suites available", type=["pdf", "txt", "docx", "csv"])
    # OperatingHours = st.file_uploader("Availability and operating time of in house facilities such as restaurants, gyms, etc", type=["pdf", "txt", "docx", "csv"])
    # Services = st.file_uploader("Availability of room services, shuttle service, concierge, etc", type=["pdf", "txt", "docx", "csv"])
    # Additional = st.file_uploader("Additional services and Unique features", type=["pdf", "txt", "docx", "csv"])
    # Policy = st.file_uploader("Hotel Policy", type=["pdf", "txt", "docx", "csv"])
    # Dining = st.file_uploader("Hotel's food and dining", type=["pdf", "txt", "docx", "csv"])
    files = [hotel]
    if st.button("Upload Files"):
        for file in files:
            if file is not None:
                st.write("Uploaded file:", file.name)
                # Change the save path to 'data' directory
                save_path = os.path.join("data", file.name)
                # Check if 'data' directory exists, if not, create it
                if not os.path.exists('data'):
                    os.makedirs('data')
                save_uploaded_file(file, save_path)
    
    if st.button("Submit"):
            st.write("Done.")
            subprocess.Popen(["streamlit", "run", "new1.py"], shell=True)
            st.rerun()
            st.stop()
if __name__ == "__main__":
    main()