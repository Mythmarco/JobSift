import requests
import os

def fetch_data(job_id, candidate_id): # Fetch Job Description and resume

  url_job = 'https://bepc.backnetwork.net/JobSiftBeta/assets/php/equalizer.php'
  data_job = {"job": job_id, "get_description": "1"}
  response_job = requests.post(url_job, data=data_job)
  job_description = response_job.text

  url_resume = 'https://bepc.backnetwork.net/JobSiftBeta/assets/php/job.php'
  data_resume = {"candidate": candidate_id}
  response_resume = requests.post(url_resume, data=data_resume)
  candidate_resume = response_resume.text

  os.system('cls')
  print(candidate_resume)

  return job_description, candidate_resume