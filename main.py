import random
from replit import clear
from art import logo
from art import vs
from game_data import data
a_icon={}
b_icon={}
a_number=""
b_number=""
score=0
####################
def picking_up():
 icon={}
 icon=random.choice(data)
 return icon
####################
def compare(a_dict,b_dict):
  term_1=a_dict['follower_count']
  term_2=b_dict['follower_count']
  if term_1>term_2:
    return "a"
  else:
    return "b"
####################
a_icon=random.choice(data)
should_continue=True
while should_continue:
 clear() 
 print(logo)
 if score>0:
   print(f"you're right.your current score:{score}.") 
 b_icon=picking_up()
 result=compare(a_icon,b_icon)
 print(f"Compare A: {a_icon['name']},{a_icon['description']},from {a_icon['country']}.")
 print(vs)
 print(f"Against B : {b_icon['name']},{b_icon['description']},from {b_icon['country']}.")
 guess=input("who has more followers? Type 'A' or 'B' ?")
 if guess== result:
    score+=1
    a_icon=b_icon
 else:
  should_continue=False
  clear()
  print(logo)
  print("sorry!that's wrong.final score:0") 
  
 

  
  