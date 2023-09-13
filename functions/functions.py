prompt_function = [
  {
    "name": "json_answer",
    "description": "this function arranges the different paragraphs into a json format for later use",
    "parameters": {
      "type": "object",
      "properties": {
        "requirements_rating":{
          "type": "number",
          "description": "the rating (out of 10) from the requirements"
        },
        "desired_elements_rating": {
          "type": "number",
          "description": "the rating (out of 10) from the desired elements"
        },
        "viability_summary":{
          "type": "string",
          "description": "a 2-3 paragraph summary of the candidate's viability for the job description"
        },
        "requirements_table":{
          "type": "array",
          "items": {
            "type": 'object',
            "properties": {
              "category": {
                "type": "string",
                "description": "The desired item category.",
              },
              "score": {
                "type": "number",
                "description": "Score given to the category.",
              },
              "explanation": {
                "type": "string",
                "description": "Explanation for the score given.",
              },
            },
            "required": ["category", "score", "explanation"]
          },
        },
        "desired_elements_table":{
          "type": "array",
          "items": {
            "type": 'object',
            "properties": {
              "category": {
                "type": "string",
                "description": "The desired item category.",
              },
              "score": {
                "type": "number",
                "description": "Score given to the category.",
              },
              "explanation": {
                "type": "string",
                "description": "Explanation for the score given.",
              },
            },
            "required": ["category", "score", "explanation"],
          },
        }
      },
      "required": ["requirements_rating", "desired_elements_rating", "viability_summary","requirements_table","desired_elements_table"]
    }
  }
]