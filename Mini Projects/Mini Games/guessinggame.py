#GUESSING GAME
import random

options = ["1", "2" ,"3", "4", "5", "6", "7", "8", "9","0"]
secret_number = int(random.choice(options))
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter your guess number between 0 to 9: "))
    guess_count +=1
    if guess == secret_number:
        print(f"{secret_number} is the correct number\n YOU WON!!!")
        break
else:
    print(f"{secret_number} is the correct number\n YOU LOSE!!!")