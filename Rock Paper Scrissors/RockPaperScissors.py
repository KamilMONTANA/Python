import random

options = ["rock", "paper", "scissors"]

rock = """
   _______
--'  ____ )
     (_____ )
     (_____ )
     (____  )
--.___(___)
"""

paper = """
   _______
--'  ____ )____
        ______ )
       _______ )
      _______ )
--.__________)
"""

scissors = """
   _______
--'  ____ )____
        ______ )
     __________)
     (____  )
--.___(___)
"""

game_images = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors!")

user_choice = int(input("Enter 0 for rock, 1 for paper, or 2 for scissors: "))
computer_choice = random.randint(0, 2)

if user_choice > 2 and user_choice < 0:
    print("Invalid choice. Please enter 0, 1, or 2.")
else:
    print("\nYou chose:")
    print(game_images[user_choice])
    print("\nComputer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!\n")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!\n")
    elif computer_choice > user_choice:
        print("You lose!\n")
    elif user_choice > computer_choice:
        print("You win!\n")
    else:
        print("It's a draw!\n")
