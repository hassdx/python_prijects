#calclator with python 

choices = ["+", "-", "*", "/"] 

while True:
    start = input("type s/to start, or q/to quit: ")
    if start == "s":

        while True:
            user_choice = input("type your choice to start ( '+' or '-' or '*' or '/' ) or Q to quit: ").lower()
            if user_choice == "q":
                break

            if user_choice not in choices:
                print("you type somthing wrong, try again.")
                continue

            elif user_choice == choices[0]:

                num1 = input("type your first number: ")
                if num1.isdigit():
                    num2 = input("type your second number: ")
                    if num2.isdigit():
                        num1 = int(num1)
                        num2 = int(num2)

                        def add():
                            return num1 + num2

                        print(add())
                    else:
                        print("(" + num2, ") is not a number. try again")
                else:
                    print("(", num1, ") is not a number. try again")

            elif user_choice == choices[1]:

                num1 = input("type your first number: ")
                if num1.isdigit():
                    num2 = input("type your second number: ")
                    if num2.isdigit():
                        num1 = int(num1)
                        num2 = int(num2)

                        def add():
                            return num1 - num2

                        print(add())
                    else:
                        print("(" + num2, ") is not a number. try again")
                else:
                    print("(", num1, ") is not a number. try again")

            elif user_choice == choices[2]:

                num1 = input("type your first number: ")
                if num1.isdigit():
                    num2 = input("type your second number: ")
                    if num2.isdigit():
                        num1 = int(num1)
                        num2 = int(num2)

                        def add():
                            return num1 * num2

                        print(add())
                    else:
                        print("(" + num2, ") is not a number. try again")
                else:
                    print("(", num1, ") is not a number. try again")

            elif user_choice == choices[3]:

                num1 = input("type your first number: ")
                if num1.isdigit():
                    num2 = input("type your second number: ")
                    if num2.isdigit():
                        num1 = int(num1)
                        num2 = int(num2)

                        def add():
                            return num1 / num2

                        print(add())
                    else:
                        print("(" + num2, ") is not a number. try again")
                else:
                    print("(", num1, ") is not a number. try again")
    
    elif start == "q":
        break
    
