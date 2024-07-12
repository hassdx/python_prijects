import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissor"]
print("welcome to the game, enjoy!!!!")

while True:
    computer_number = random.randint(0, 2)
    computer_pick = options[computer_number]

    user_pick = input("\ntype your choice (rock/ paper/ scissor) or Q o quit:  ").lower()
    if user_pick == "q":
        break

    elif user_pick not in options:
        continue


    if user_pick == "rock" and computer_pick == "scissor":
        user_score += 1
        print("you picked", user_pick)
        print("computer picked", computer_pick)
        print("you won")



    elif user_pick == "paper" and computer_pick == "rock":
        user_score += 1
        print("you picked", user_pick)
        print("computer picked", computer_pick)
        print("you won")


    elif user_pick == "scissor" and computer_pick == "paper":
        user_score += 1
        print("you picked", user_pick)
        print("computer picked", computer_pick)
        print("you won")

    elif user_pick == computer_pick:
        print("you both picked the same, try again")

    else:
        computer_score += 1
        print("you picked", user_pick)
        print("computer picked", computer_pick)
        print("computer win")


def final_score():
    if user_score > computer_score:
        print("you won", user_score, "times.")
        print("computer won", computer_score, "times.")
        print("you won this game<<<<<<<<<<<<<")
    elif user_score < computer_score:
        print("you won", user_score, "times.")
        print("computer won", computer_score, "times.")
        print("computer won this game<<<<<<<")
    elif user_score == computer_score:
        print("you won", user_score, "times.")
        print("computer won", computer_score, "times.")
        print("you both equaled")


final_score()
