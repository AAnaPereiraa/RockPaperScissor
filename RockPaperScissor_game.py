import random, figures

game_on = True
username = input("Welcome\n\nWhat's your name?\n")
print(f"\nHello {username.capitalize()}!\n\n")

while game_on:   
    play = str(input("Are you ready (Yes/No)? "))
    
    try:
        if play.lower() == "no":
            game_on = False
            print("\nCome back when you are ready..see you soon!!!\n")

        elif play.lower() == "yes":
            while game_on:
                try:
                    print(f"\n{username.capitalize()}!\n\nPlease choose: ")
                    print("0 - Rock")
                    print("1 - Paper")
                    print("2 - Scissor")

                    choice = int(input("\nPlease insert your choice.\n"))
                    computer = random.randint(0, 2)

                    win = [(0, 2), (1, 0), (2, 1)]
                    loose = [(0, 1), (1, 2), (2, 0)]
                    draw = [(0, 0), (2, 2), (1, 1)]

                    game = (choice, computer)

                    print(f"\n{username.capitalize()}\n", figures.figures[choice])
                    print("\nComputer\n", figures.figures[computer])

                    if game in draw:
                        print("\n\nIt's a draw!!!\n")
                    elif game in win:
                        print("\n\nYou won!!!\n")
                    elif game in loose:
                        print("\n\nYou lost\n")  

                    continue_play = input(f"\n{username.capitalize()}!\n\nwould you like to play again (Y/N)? ")

                    if continue_play.lower() == "n":
                        print(f"\n{username.capitalize()}!\n\nThank you for playing...see you later!!!")
                        game_on = False
            
                except (ValueError, IndexError):
                    print("Please enter an option number")  
            
        elif play.lower() != "no" or play.lower() != "yes":
            raise ValueError()

    except (ValueError, IndexError):
        print("Please answer Yes or No")