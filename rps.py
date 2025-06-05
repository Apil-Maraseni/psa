import random
while True:
 def get_computers_choice():
    random_number = random.randint(1,3)

    options = {1:"rock", 2:"paper", 3:"scissor"}

    computers_choice = options[random_number]

    return computers_choice




 def get_user_input():

     user_input = input("Enter rock/paper/scisssor: ").lower()
     while user_input not in ["rock","paper","scissor"]:
        print("Invalid input. Please Try again.")
        user_input = input("Enter rock/paper/scisssor: ").lower()
     return user_input



 def get_result(user_pick, computer_pick):
    if computer_pick == user_pick:
        return "draw"
    elif computer_pick== "scissor" and user_pick== "rock":
        return "win"
    elif computer_pick== "paper" and user_pick== "scissor":
        return "win"
    elif computer_pick== "rock" and user_pick== "paper":
        return "win"
    else:
        return "lose"

 computers_choice = get_computers_choice()
 user_pick = get_user_input()
 result = get_result(user_pick, computers_choice)
 print("computer chose", computers_choice)
 print("your choice",user_pick )
 print("Result is",result) 
    
