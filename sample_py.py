# Coded by Denis Sakanovic 02/02/2025 

import random

# I did this all today, so it is not refactored/ top notch code.

def sb_create():
  #['Given A = {xEN | 1 <= x <= 7}, what is the roster form?','{1,2,3,4,5,6,7}',fig_venn3,'nofig']

  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

  # s = select
  s_set = random.choices([nums, abc], weights=[.5, .5])[0]
  s_region = random.choices(['A', 'B', 'C'], weights=[.33, .33, .33])[0]
  
  starting_index = random.randint(0, 4)
  ending_index = (len(s_set) - 1 - random.randint(0, 3))

  set_l = s_set[starting_index]
  last_set_l = s_set[ending_index]
    
  countin_commas = ["{", "}"] # lol 
  question = f"Given {s_region} = {countin_commas[0]}xEN | {set_l} <= x <= {last_set_l}{countin_commas[1]}, what is the roster form?"
  
  difference = ending_index - starting_index + 1
  
  answer = []

  for i in range(difference):
    answer.append(s_set[starting_index + i]) 
  
  return question, str(answer).replace('[', '{').replace(']','}')

def create_stuff(notation, ques_type):
  
  weight_s = {'rn': [.1, .4, .5],
            'ca': [.2, .6, .2], 
            'dm': [.3, .6, .1],
            'ps': [.2, .6, .2],
            'pt': [.5, .5]}
  
  choices = [1, 2, 3]

  if notation == 'logic':
    logic = ['P', 'Q']
    n_or_v = ['^', 'v', '->', '<->']
    choices = [1, 2]
  else:
    abc = ['A', 'B', 'C']
    u_or_n = ['u', 'n']
  
  compliment = ['_', '__', '']
  
  notations = []
  
  # loop twice to get 2 expressions
  for _ in range(2):
  
    selection = int(random.choices(choices, weights=weight_s[ques_type])[0])

    region_l = []

    while len(region_l) < selection:
      
      # This is for having duplicates and no sorting 
      #index = random.randint(0, len(logic) - 1) if notation == 'logic' else random.randint(0, len(abc) - 1)
      #region_l.append(logic[index] if notation == 'logic' else abc[index])

      # this is not allowing duplicates and sorting 
      if notation == 'logic':
        index = random.randint(0, len(logic) - 1)
        if logic[index] not in region_l:
          region_l.append(logic[index])
      else:
        index = random.randint(0, len(abc) - 1)
        if abc[index] not in region_l:
          region_l.append(abc[index])

      region_l.sort()
    
    compliment_list = [compliment[int(random.choices([0, 1], weights=[0.7, 0.3])[0])] for _ in range(selection)]
    #print(f"LIST: {compliment_list}")
    
    u_or_n_list = [random.choice(n_or_v) if notation == 'logic' else random.choice(u_or_n) for _ in range(selection - 1)]

    u_or_n_list.append('')

    #print(compliment_list)
    #print(u_or_n_list)
    #print(region_l)
      
    dnf_notation = ""

    for i in range(selection):
      dnf_notation = f"{dnf_notation}{compliment_list[i]}{region_l[i]}{u_or_n_list[i]}"
 
    notations.append(dnf_notation)
    
    # Trying to create a logical statement w/ two expressions


    if notation == 'logic' and len(notations) == 2:
      always_n_v = ['^', 'v', '->', '<->']
      select_one = int(random.choices([0, 1, 2, 3], weights=[.4, .4, .1, .1])[0])
      two_expressions = f"({notations[0]}){always_n_v[select_one]}({notations[1]})"

    elif notation == 'dnf' and len(notations) == 2:
      always_u_n = ['u', 'n']
      select_one = int(random.choices([0, 1], weights=[.5, .5])[0])
      two_expressions = f"({notations[0]}){always_u_n[select_one]}({notations[1]})"

  return notations, two_expressions
  #return dnf_notation

if __name__ == "__main__":

  q, a = sb_create()

  print('################################')
  print(q)
  print(f"Answer: {a}")
  notations, t = create_stuff('logic', 'pt')
  print('################################')
  print(f"Expression 1: {notations[0]}")
  print(f"Expression 2: {notations[1]}")
  print(f"Combined Expressions: {t}")
  print('################################')

