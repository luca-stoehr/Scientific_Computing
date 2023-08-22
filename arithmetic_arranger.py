def arithmetic_arranger(problems, solve=False):

  return arranged_problems

def limit_calculations(problems):
  num_problems = len(problems)
  if num_problems > 5:
    raise ValueError('Error: Too many problems.')
  elif num_problems <= 0:
    raise ValueError('A minimum of 1 problem is needed.')
  else:
    return True

def find_operator(problem):
  if "+" in problem:
    return True
  elif "-" in problem:
    return False
  else:
    raise ValueError('Error: Operator must be "+" or "-".')
  