import random

image = """
██████   ██████   ██████ ██   ██     ██████   █████  ██████  ███████ ██████      ███████  ██████ ██ ███████ ███████  ██████  ██████  ███████ 
██   ██ ██    ██ ██      ██  ██      ██   ██ ██   ██ ██   ██ ██      ██   ██     ██      ██      ██ ██      ██      ██    ██ ██   ██ ██      
██████  ██    ██ ██      █████       ██████  ███████ ██████  █████   ██████      ███████ ██      ██ ███████ ███████ ██    ██ ██████  ███████ 
██   ██ ██    ██ ██      ██  ██      ██      ██   ██ ██      ██      ██   ██          ██ ██      ██      ██      ██ ██    ██ ██   ██      ██ 
██   ██  ██████   ██████ ██   ██     ██      ██   ██ ██      ███████ ██   ██     ███████  ██████ ██ ███████ ███████  ██████  ██   ██ ███████ 


"""
print(image)


def compare(user, computer): #function to define the result of the game
    if user == computer:
        return "Draw!!"
    elif ((user == "rock" and computer == "scissors") or
          (user == "paper" and computer == "rock") or
          (user == "scissors" and computer == "paper")): #condition for the user win cases
        return "User Win!!"
    else:
        return "Computer win!!"

options = ["rock", "paper", "scissors"]
while True: # main loop to continue game until user wants to exit
    while True: # loop to get proper input from user
        user_choice = (input("Enter your choice Rock, Paper, Scissors\n")).lower()
        if user_choice in options: # to check if input is correct
            break
        else:
            print("Give a proper input!!")

    computer_choice = random.choice(options)
    print("User choice: ", user_choice.upper())
    print("Computer choice: ", computer_choice.upper())
    print(compare(user_choice, computer_choice))
    restart = input("Do you want to start again.\nType 'y' to restart and 'n' to exit: ").lower()
    if restart == "y": # checking if user wants to continue game or exit
        continue
    elif restart == "n":
        print("Thankyou for playing :)")
        break
    else:
        print("Wrong input. Automatically assuming exit.")
        print("Thankyou for playing :)")
        break