# <img src="static/rs2.png" width="100" height="100" style="vertical-align: middle;"> BEPC JobSift 2.1<i><span style="font-size: 0.8em;">for Recruiters</span></i>

## Overview
The BEPC JobSift is a Streamlit application designed to enhance the resume - Job Description review. It accepts both a JobID and a Resume ID from Bullhorn, and applies a chat completion using gpt 4.0 Turbo to provide a rating and a summary of the candidate's viability for the Job Description. The app's backend is built in php and a php connection to bullhorn which we use as an endpoint through a request in python. 

## Installation

This app requires Python 3.10 or later. You will also need to install the necessary Python libraries, which are listed in the requirements.txt file. You can install these dependencies with pip:

Copy code
```pip install -r requirements.txt```
Usage
To run the app, navigate to the application's directory and execute the following command:

Copy code
```streamlit run resume_styler.py```

The application will then be accessible in your web browser at http://localhost:8501.

## Usage:
Enter the Job ID in the provided text area.
Enter the candidate ID in the provided text area.
Click the 'Evaluate' button to generate a summary of the candidate's viability and the score of the candidate.

## Features
Uses BEPC API connection to Bullhorn to pull Job Description and Candidate Resume.
Compares the two documents and generates a summary of the candidate's viability and the score of the candidate.

## Note
This app is not intended to be used for any other purpose than to demonstrate the capabilities of the BEPC API and GPT 4 Turbo It is not intended to be used in a production environment.

## Changelog
This New verison adds seed, for reproducible outputs as per : https://platform.openai.com/docs/guides/text-generation/reproducible-outputs

## Author

- [Marco Saenz]((https://github.com/Mythmarco))

## License

This project is [MIT licensed](./LICENSE).
