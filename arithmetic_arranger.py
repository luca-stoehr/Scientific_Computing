def arithmetic_arranger(problems, solve=False):
  if limit_calculations(problems):
    return 'Error: Too many problems.'
  first_line = [None] * len(problems)
  second_line = [None] * len(problems)
  third_line = [None] * len(problems)
  if solve:
    forth_line = [None] * len(problems)
  idx = 0
  for problem in problems:
    operator = find_operator(problem)
    if isinstance(operator, str):
      return "Error: Operator must be '+' or '-'."
    check_syn = check_syntax(problem, operator)
    if isinstance(check_syn, str):
      return check_syn
    (first, second) = calc_separator(problem, operator)
    first_line[idx] = first
    second_line[idx] = second
    block_length = string_formatter(first_line[idx], second_line[idx])
    third_line[idx] = "-" * block_length
    if operator:
      if solve:
        forth_line[idx] = int(first_line[idx]) + int(second_line[idx])
        forth_line[idx] = "{}{}".format(" " * (block_length - len(str(forth_line[idx]))), forth_line[idx])
      second_line[idx] = "{}{}{}".format("+"," " * (block_length - len(second_line[idx]) - 1), second_line[idx])
    else:
      if solve:
        forth_line[idx] = int(first_line[idx]) - int(second_line[idx])
        forth_line[idx] = "{}{}".format(" " * (block_length - len(str(forth_line[idx]))), forth_line[idx])
      second_line[idx] = "{}{}{}".format("-"," " * (block_length - len(second_line[idx]) - 1), second_line[idx])
    first_line[idx] = "{}{}".format(" " * (block_length - len(first_line[idx])), first_line[idx])
    idx += 1
  arranged_problems_base = "\n".join(["    ".join(first_line), "    ".join(second_line), "    ".join(third_line)])
  if solve:
    arranged_problems = "\n".join([arranged_problems_base, "    ".join(forth_line)])
  else:
    arranged_problems = arranged_problems_base
  return arranged_problems


def limit_calculations(problems):
  num_problems = len(problems)
  if num_problems > 5:
    #raise ValueError('Error: Too many problems.')
    return True
  # elif num_problems <= 0:
    # raise ValueError('A minimum of 1 problem is needed.')
  # else:
    # return True

def find_operator(problem):
  if "+" in problem:
    return True
  elif "-" in problem:
    return False
  else:
    # raise ValueError('Error: Operator must be "+" or "-".')
    return "Error: Operator must be '+' or '-'."
  
def check_syntax(problem, operator):
  (first,second) = calc_separator(problem, operator)
  if first.isdigit() == False or second.isdigit() == False:
    # raise ValueError('Error: Numbers must only contain digits.')
    return 'Error: Numbers must only contain digits.'
  if len(first) > 4 or len(second) > 4:
    # raise ValueError('Error: Numbers cannot be more than four digits.')
    return 'Error: Numbers cannot be more than four digits.'
  return True
  
def calc_separator(problem, operator):
  if operator:
    ind_op = problem.find('+')
  else:
    ind_op = problem.find('-')
  if problem[ind_op-1] != " " or problem[ind_op+1] != " ":
    raise ValueError('Error: Include a space before and after the operator.')
  first = problem[:ind_op-1]
  second = problem[ind_op+2:]
  return first, second

def long_operand(first, second):
  # returns positive integer if first is larger, negative integer if second is larger and zero if both are the same
  return int(first) - int(second)

def string_formatter(first, second):
  diff_len_oper = long_operand(first,second)
  if diff_len_oper == 0:
    block_len = len(first) + 2
  elif diff_len_oper < 0:
    block_len = len(second) + 2
  else:
    block_len = len(first) + 2
  return block_len
    