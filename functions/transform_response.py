# this function transforms the output from the response as readable strings for easy coding and formatting
def transform_response(
  requirements_table, 
  desired_elements_table 
  ):

  requirements_table_start = '<p><table class="table"><tr><th>Category</th><th>Score</th><th>Explanation</th></tr>'
  requirements_table_middle = ''
  requirements_table_end = '</table></p>'

  for table_row in requirements_table: #here is where we convert the requirements array into the html format
    requirements_table_middle += '<tr>'
    for index, value in table_row.items():
      new_row = '<td>' + str(value) + '</td>'
      requirements_table_middle += new_row
    requirements_table_middle += '</tr>'

  desired_table_start = '<p><table class="table"><tr><th>Category</th><th>Score</th><th>Explanation</th></tr>'
  desired_table_middle = ''
  desired_table_end = '</table></p>'

  for table_row in desired_elements_table: #here is where we convert the desired elements array into the html format
    desired_table_middle += '<tr>'
    for index, value in table_row.items():
      new_row = '<td>' + str(value) + '</td>'
      desired_table_middle += new_row
    desired_table_middle += '</tr>'

  requirements_table_full = requirements_table_start + requirements_table_middle + requirements_table_end
  desired_table_full = desired_table_start + desired_table_middle + desired_table_end

  return [
    requirements_table_full,
    desired_table_full,
  ]