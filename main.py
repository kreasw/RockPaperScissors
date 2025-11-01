import random

print("Welcome to ROCK PAPER SCISSORS")

play_again = "Y"

while play_again.upper() == "Y": # the loop so game can repeat
    user_answer = input("Pick ROCK, PAPER or SCISSORS: ")
    user_answer_upper = user_answer.upper()
    print("")


    computer = random.choice(["ROCK", "PAPER", "SCISSORS"]) # computer chooses randomly

    print("you choose " + user_answer_upper)
    print("Computer chose " + computer)
    print("")

    if user_answer_upper == computer:
        print("Tie")

    elif (user_answer_upper == "ROCK" and computer == "SCISSORS") or \
        (user_answer_upper == "PAPER" and computer == "ROCK") or \
        (user_answer_upper == "SCISSORS" and computer == "PAPER"):
        print("you win!")

    elif (user_answer_upper == "ROCK" and computer == "PAPER") or \
        (user_answer_upper == "PAPER" and computer == "SCISSORS") or \
        (user_answer_upper == "SCISSORS" and computer == "ROCK"):
        print("You lose!")

    else: # If the user entered something invalid
        print("you choose a incorrect answer")

    print("")


    while True: # Keeps asking the user if they want to play again. If they enter anything else than Y or N the program will keep asking until the user gives a valid input
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y" or play_again == "N":
            break
        else:
            print("Wrong input")

