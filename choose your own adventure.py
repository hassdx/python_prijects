# choose your adventure

user_name = input("type your name: ")
while True:
    user_stats = input("welcome " + user_name + " type S to start, or Q to quit: ").lower()

    if user_stats == "s":
        print("hello", user_name, "welcome to he game")

        while True:
            print("you going to start in the middle of the forest, choose your way to survive. there is no go back when you you chose you destination")
            answer = input("print L to go left, R to go right, F to go forward: ").lower()
            if answer == "l":
                print("you go left, now you came to a bridge, would you like to cross on the bridge or turn right.")
                answer = input("print cross to cross, or turn to turn right: ").lower()
                if answer == "cross":
                    print(
                        "you cross the bride, now you came to a river, would you like to made a wooden boat or swim in the river. ")
                    answer = input("print made to made a wooden boat, or swim to swim in the river: ").lower()
                    if answer == "made":
                        print("you made a boat and you survived in the river, then you find the city")
                        print("NIIIIIIIIIIIIIICE WOOOOOOOOOORK!!!!!!!!!")
                        quit()
                    elif answer == "swin":
                        print("you swim in the river and crocodile killed you.")
                        print("you lose<<<<<<<<<<<<")
                        break
                elif answer == "turn":
                    print("You turn right and you find a bear and it kills you ")
                    break

            elif answer == "r":
                print(
                    "you go right, and you find a mountain, would you like to hike the mountain or turn left and find an other way.  ")
                answer = input("print hike/ to hike the mountain, or turn/ to turn left: ").lower()
                if answer == "hike":
                    print("You chose to climb the mountain and you don't have any equipment so you died.")
                    print("you lose<<<<<<<<<")
                    break
                elif answer == "turn":
                    print("you turned left and you get lost in the woods")
                    print("you lose<<<<<<<<<<<")
                    break

            elif answer == "f":
                print(
                    "you chose to go forward and you came in front of a cave, would you like to discover the cave or take the road near than you?")
                answer = input("print d/ to discover the cave, or take/ to take the next road: ").lower()
                if answer == "d":
                    print(
                        "you entered the cave and you find a hole would you like to discover the hole also, or wait into the cave? ")
                    answer = input("print d/ to discover the hole, or wait/ to wait into the cave: ").lower()
                    if answer == "d":
                        print("you got stocked in the hole.")
                        print("you lose<<<<<<<<<<<")
                        break
                    elif answer == "wait":
                        print("a quick earth happened and you died into the cave during you wait.")
                        print("you lose<<<<<<<<<<<")
                        break
                elif answer == "take":
                    print("you chose to walk in the next road and you get lost in the forest.")
                    print("you lose<<<<<<<<<<<")
                    break

            else:
                print("you type somthing not available, try again.")
                continue

    elif user_stats == "q":
        print("you quit the game")
        break

    elif user_stats != "s" or "q":
        continue
