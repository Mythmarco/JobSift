prompt_li_function = [
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
            "education":{ # REQUIRED EDUCATION
              "type": "object",
              "properties": {
                "required": {
                  "type": "boolean",
                  "description": "If the job description states that education is needed, mark this as true.",
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
            "Experience": { # REQUIRED EXPERIENCE
              "type": "object",
              "properties": {
                "required": {
                  "type": "boolean",
                  "description": "If the job description states that experience is needed, mark this as true.",
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
              "required": ["required", "score", "explanation"]
            },
            "Certifications / Licenses": { # REQUIRED CERTIFICATIONS OR LICENSES
              "type": "object",
              "properties": {
                "required": {
                  "type": "boolean",
                  "description": "If the job description states that certifications or licenses are needed, mark this as true.",
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
            }
          },
          "required": ["education"]
        },
        "desired_elements_table": {
          "type": "object",
          "properties": {
            "education":{ # PREFERRED EDUCATION
              "type": "object",
              "properties": {
                "required": {
                  "type": "boolean",
                  "description": "If the job description states that a certain education is preferred or nice to have, mark this as true.",
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
              "required": ["score", "explanation"]
            },
            "Experience": { # PREFERRED EXPERIENCE
              "type": "object",
              "properties": {
                "required": {
                  "type": "boolean",
                  "description": "If the job description states any preferred experience, mark this as true.",
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
                "required": {
                  "type": "boolean",
                  "description": "If the job description states any preferred certifications or licenses, mark this as true.",
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
            }
          },
          "required": ["education"]
        }
      },
      "required": ["viability_summary","requirements_table","desired_elements_table"]
    }
  }
]