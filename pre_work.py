#########################
###### Raul Lara ########
#########################


#question 1
def hello_name(user_name):
  user_name = input("Enter USERNAME")
  print('hello_', user_name)

#question 2
def first_odds():
  for i in range (0, 101):
    if (i % 2 != 0 ):
      print(i)
      
#question 3
def max_num_in_list(a_list):
  maxValue = 0
  size = len(a_list)
  for i in range(size):
    if(a_list[i] > maxValue):
      maxValue = a_list[i]

#question 4
def is_leap_year(a_year):
  if(a_year % 4 == 0) & (a_year % 100 != 0) | (a_year % 400 == 0):
    return True
  else:
    return False

#question 5
def is_consecutive(a_list):
  difference = 1
  size = len(a_list)
  for i in range(size):
    if(a_list[i] - a_list[i-1] != 1):
      return False
    else:
      return True