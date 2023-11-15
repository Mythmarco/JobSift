import streamlit as st
import os
import base64 
from werkzeug.utils import secure_filename
from utils import fetch_data, calculate_score

# Initialize Streamlit and set page configurations
st.set_page_config(page_title="BEPC-JobSift", page_icon="static/logo.png", layout='wide')

# Function to read binary data and convert to base64
def get_image_base64(image_path):
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Convert images to base64 and include in HTML
sr2new = get_image_base64('static/rs2.png')
st.markdown(
    f"""
    <div class="container">
        <h2 class="text-center mt-4">
            <img src="data:image/png;base64,{sr2new}" width="50" height="50" class="d-inline-block align-top" alt="">
            JobSift <span style="font-style: italic; font-size: 17px;">for recruiting V2.1</span>
        </h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# User Input via Streamlit widgets
job_type = st.selectbox('Select Job Type', ['Professional', 'Light Industrial'])
job_id = st.text_input('1.- Enter the Job ID')
candidate_id = st.text_input('2.- Enter the Candidate ID')  # Changed 'candidate' to 'candidate_id' for consistency
experience = st.text_input('3.- Enter the Candidate Experience')
keywords = st.text_input('4.- Enter the Keywords')

# Evaluate Resume Button
if st.button('Evaluate Resume'):
    with st.spinner('Evaluating...'):
        # Fetch Job Description and Candidate Resume
        job_description, candidate_resume = fetch_data(job_id, candidate_id)
        
        
        # Calculate Score and Summary
        score_summary = calculate_score(job_description, candidate_resume, job_type)
        
        # Display Results
        st.markdown(f"### Score and Summary:\n{score_summary}")
        st.success("Resume processing completed! To transform another file, please refresh the page (press F5).")

# Footer
st.markdown("""
<footer class="footer mt-auto py-3">
    <div class="container text-center">
        <p class="text-muted">
            Copyright © 2023 | BEPC Incorporated | All Rights Reserved |
            <a href="Privacy_Policy_Link">Privacy Policy</a> |
            <a href="Cybersecurity_Link">Cybersecurity</a> |
            <a href="HIPAA_Link">HIPAA</a>
            |  MSMMXXIII
        </p>
    </div>
</footer>
""", unsafe_allow_html=True)