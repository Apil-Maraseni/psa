# To create a game of rock paper scissors using the concept of oop
import random
class Game:
    def __init__(self):
        self.computer_pick = self.get_computer_pick()  #get computer pick
        self.user_pick = self.get_user_pick() 
        self.result = self.get_result()


    def get_computer_pick(self):
        random_number = random.randint(1,3)

        options = {1: 'rock', 2: 'paper', 3: 'scissors'}
        return options[random_number]
    
    def get_user_pick(self):
      while True:

        user_pick = input("Enter rock/paper/scissors:")
        if user_pick in ('rock', 'paper', 'scissors'):
           return user_pick.lower()
        else:
           print("Invalid input. Try using 'rock'/'paper'/'scissors'")

    def get_result(self):
       if self.computer_pick == self.user_pick:
          return 'draw'
       elif self.user_pick == 'paper' and self.computer_pick == 'rock':
          return 'win'
       elif self.user_pick == 'rock' and self.computer_pick == 'scissors':
          return 'win'
       elif self.user_pick == 'scissors' and self.computer_pick == 'paper':
          return 'win'

       else:
          return 'lose'

    def print_result(self):
       print(f"Computer's pick: {self.computer_pick}")
       print(f"Your pick: {self.user_pick}")
       print(f"You {self.result}")      
while True:
   
   game = Game()
   game.print_result()

   play_again = input("Do you want to play again? (y/n):").lower()

   if play_again != 'y':
      print("Thanks for Playing :)")
      break