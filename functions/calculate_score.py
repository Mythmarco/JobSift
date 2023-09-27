import os
import openai
import json
from dotenv import load_dotenv 
from functions.functions import prompt_function

load_dotenv()
openai.api_key=os.getenv("openai.api_key")

def calculate_score(job_description, candidate_resume, job_type): # api call function to chatgpt

  prompt_guidelines = '' # variable to store the rules of the prompt
  if job_type == 'Light Industrial':  # switch to handle the rules of the prompt
    with open('helpers/light_industrial.txt', 'r') as f:
      prompt_guidelines = f.read()
  elif job_type == 'Professional':
    with open('helpers/professional.txt', 'r') as f:
      prompt_guidelines = f.read()

  score_summary = openai.ChatCompletion.create( # Make API call
  model = "gpt-4",
  messages = [
    {"role":"system", "content":"You are an expert recruiting AI.\
      Evaluate how a candidate's resume matches a job description\
      based on the following guidelines:"},
    {"role":"user", "content":f"Job Type: {job_type}"},
    {"role":"user", "content":f"{prompt_guidelines}"},
    {"role":"user", "content":"Provide a score from 0 to 10 representing how well\
      the candidate matches the job description for both Requirements and Desired elements."},
    {"role":"user", "content":f"Job Description: {job_description}"},
    {"role":"user", "content":f"Candidate Resume: {candidate_resume}"},
    {"role":"user", "content":f"Provide a 2-3 paragraph summary of the candidate's\
      viability for the job description."},
    {"role":"user", "content":"Create a list of the required categories,\
      the score you gave, and the explanation for that score given"},
    {"role":"user", "content":"Create a list of the desired categories,\
      the score you gave, and the explanation for that score given"},
  ],
  temperature = 0, # The temperature parameter controls the randomness of the generated output.
  functions = prompt_function,
  function_call = {
    "name": "json_answer"
  }
  )
  
  return json.loads(score_summary['choices'][0]['message']['function_call']['arguments']) # Extract the summary text from the response