import random

start = ["s", "q"]
guesses = 0

while True:
    top_of_number = input("type rang of the number:  ")
    if top_of_number.isdigit():
        top_of_number = int(top_of_number)

        while True:
            start_status = input("welcome to the gess game, print s/ start the the game, or q/ to quit the game:  ").lower()
            if start_status not in start:
                continue
            elif start_status == start[0]:
                print("let's start the game<<<<<<")
                random_number = random.randint(0, top_of_number)
                random_number = str(random_number)

                while True:
                    user_number = input("type your number: ")
                    if user_number.isdigit():
                        var = user_number == int(user_number)
                        guesses += 1
                        if user_number == random_number:
                            print("you got it!!!! ")
                            break

                        elif user_number < random_number:
                            print("you were below the number . ")

                        elif user_number > random_number:
                            print("you were above the number . ")

                        else:
                            print("your numer must be positive ")

                    else:
                        print(user_number, "is not a number.")

                print("you got the random number in ", guesses, "guesses.")
                break

            elif start_status == start[1]:
                print("you quit the game")
                break
        break
    else:
        print(top_of_number, "is not a number.")
        continue

