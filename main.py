import random

print("Welcome to ROCK PAPER SCISSORS")

play_again = "Y"

while play_again.upper() == "Y":
    user_answer = input("Pick ROCK, PAPER or SCISSORS: ")
    user_answer_upper = user_answer.upper()
    print("")


    computer = random.choice(["ROCK", "PAPER", "SCISSORS"])

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

    else:
        print("you choose a incorrect answer")

    print("")


    play_again = input("Do you want to play again? (Y/N)")
