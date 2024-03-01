#ROCK,PAPER AND SCISSORS

import random #including random library

def get_choices(): #get_choices is a function
    player_choice = input("Enter your choice (rock/paper/scissors): ")
    options = ["rock", "paper", "scissors"] #options is a list of strings
    computer_choice = random.choice(options) 
    choice = {"player": player_choice, "computer": computer_choice} #choices is a dictionary here
    return choice

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors!!! YOU win"
        else:
            return "Paper covers Rock!!!Computer wins"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock!!! YOU win"
        else:
            return "Scissors cuts paper!!!Computer wins"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors!!! Computer wins"
        else:
            return "Scissors cuts paper!!!You win"
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)