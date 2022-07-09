import random

user_wins = 0
computer_wins = 0
user_computer_ties = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
       continue

    random_number = random.randint(0, 2)
    # rock: 0 ,paper: 1 scissors: 2
    computer_pick = options[random_number]
    print("Computer chosed", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
       print("You won your opponent!")
       user_wins += 1
       continue

    elif user_input == "paper" and computer_pick == "rock":
       print("You won your opponent!")
       user_wins += 1
       continue
   
    elif user_input == "scissors" and computer_pick == "paper":
       print("You won your opponent!")
       user_wins += 1
       continue
    

    if user_input == "rock" and computer_pick == "rock":
       print("You TIED with your opponent!")
       user_computer_ties += 1
       continue

    elif user_input == "paper" and computer_pick == "paper":
       print("You TIED with your opponent!")
       user_computer_ties += 1
       continue
   
    elif user_input == "scissors" and computer_pick == "scissors":
       print("You TIED with your opponent!")
       user_computer_ties += 1
    else:
     print("You lost to your opponent!")
     computer_wins += 1
     

print("YOU WON", user_wins, "times.")
print("THE COMPUTER WON", computer_wins,"times.")
print(user_computer_ties,"times")
print("See you!") 

    