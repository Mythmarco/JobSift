prompt_p_function  = [
  {
    "name": "json_answer",
    "description": "this function arranges the different paragraphs into a json format for later use",
    "parameters": {
      "type": "object",
      "properties": {
        "viability_summary": {
          "type": "string",
          "description": "a 2-3 paragraph summary of the candidate's viability for the job description"
        },
        "requirements_table": {
          "type": "object",
          "properties": {
            "Experience": { # REQUIRED EXPERIENCE
              "type": "object",
              "properties": {
                "measurable": {
                  "type": "boolean",
                  "description": "If the job description states required or must have experience, mark this as true.",
                },
                "score": {
                  "type": "number",
                  "description": "Score given to the experience category, based on the required categories, the minimum score is 0 and the maximun is 10.",
                },
                "explanation": {
                  "type": "string",
                  "description": "Explanation for the score given.",
                }
              },
              "required": ["required","score", "explanation"]
            },
            "Education":{ # REQUIRED EDUCATION
              "type": "object",
              "properties": {
                "measurable": {
                  "type": "boolean",
                  "description": "If the job description states required or must have education, mark this as true.",
                },
                "score": {
                  "type": "number",
                  "description": "Score given to the education category, based on the required categories, the minimum score is 0 and the maximun is 10.",
                },
                "explanation": {
                  "type": "string",
                  "description": "Explanation for the score given.",
                }
              },
              "required": ["required", "score", "explanation"]
            },
            "Certifications / Licenses": { # REQUIRED CERTIFICATIONS OR LICENSES
              "type": "object",
              "properties": {
                "measurable": {
                  "type": "boolean",
                  "description": "If the job description states required or must have certifications / licenses, mark this as true.",
                },
                "score": {
                  "type": "number",
                  "description": "Score given to the certifications or licenses category, based on the required categories, the minimum score is 0 and the maximun is 10.",
                },
                "explanation": {
                  "type": "string",
                  "description": "Explanation for the score given.",
                }
              },
              "required": ["required", "score", "explanation"]
            },
            "Skills": { # REQUIRED skills
              "type": "object",
              "properties": {
                "measurable": {
                  "type": "boolean",
                  "description": "If the job description states required or must have skills, mark this as true.",
                },
                "score": {
                  "type": "number",
                  "description": "Score given to the skills category, based on the required categories, the minimum score is 0 and the maximun is 10.",
                },
                "explanation": {
                  "type": "string",
                  "description": "Explanation for the score given.",
                }
              },
              "required": ["required", "score", "explanation"]
            }
          },
          "required": []
        },
        "desired_elements_table": {
          "type": "object",
          "properties": {
            "Experience": { # PREFERRED EXPERIENCE
              "type": "object",
              "properties": {
                "measurable": {
                  "type": "boolean",
                  "description": "return true if the job description mentions any kind of preferred experience.",
                },
                "score": {
                  "type": "number",
                  "description": "Score given to the education category, based on the preferred categories, the minimum score is 0 and the maximun is 10.",
                },
                "explanation": {
                  "type": "string",
                  "description": "Explanation for the score given.",
                }
              },
              "required": ["required", "score", "explanation"]
            },
            "Education":{ # PREFERRED EDUCATION
              "type": "object",
              "properties": {
                "measurable": {
                  "type": "boolean",
                  "description": "return true if the job description mentions any kind of preferred education.",
                },
                "score": {
                  "type": "number",
                  "description": "Score given to the education category, based on the preferred categories, the minimum score is 0 and the maximun is 10.",
                },
                "explanation": {
                  "type": "string",
                  "description": "Explanation for the score given.",
                }
              },
              "required": ["required", "score", "explanation"]
            },
            "Certifications / Licenses": { # PREFERRED CERT OR LICENSES
              "type": "object",
              "properties": {
                "measurable": {
                  "type": "boolean",
                  "description": "return true if the job description mentions any kind of preferred certifications / licenses.",
                },
                "score": {
                  "type": "number",
                  "description": "Score given to the certifications or licenses category, based on the preferred categories, the minimum score is 0 and the maximun is 10.",
                },
                "explanation": {
                  "type": "string",
                  "description": "Explanation for the score given.",
                }
              },
              "required": ["required", "score", "explanation"]
            },
            "Skills": { # PREFERRED skills
              "type": "object",
              "properties": {
                "measurable": {
                  "type": "boolean",
                  "description": "return true if the job description mentions any kind of preferred skills.",
                },
                "score": {
                  "type": "number",
                  "description": "Score given to the skills category, based on the preferred categories, the minimum score is 0 and the maximun is 10.",
                },
                "explanation": {
                  "type": "string",
                  "description": "Explanation for the score given.",
                }
              },
              "required": ["required", "score", "explanation"]
            }
          },
          "required": []
        }
      },
      "required": ["viability_summary","requirements_table","desired_elements_table"]
    }
  }
]