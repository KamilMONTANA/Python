from logo import logo
import random

print(logo)


def random_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)


while True:
    print("Choose the difficulty:")
    print("1. Easy: 10 attempts")
    print("2. Medium: 5 attempts")
    print("3. Hard: 3 attempts")
    difficulty = input("Enter your choice ( 1, 2, 3 ): ")

    if difficulty == "1":
        attempts = 10
    elif difficulty == "2":
        attempts = 5
    elif difficulty == "3":
        attempts = 3
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    random_number = random_number()
    print(f"Random number: {random_number}")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == random_number:
            print("""
            ####################################
            # You guessed the number! You win! #
            ####################################
            \n""")
            break
        elif guess < random_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")
        attempts -= 1
    else:
        print("You've run out of attempts. You lose!")
        print(f"The number was: {random_number}")
        break
