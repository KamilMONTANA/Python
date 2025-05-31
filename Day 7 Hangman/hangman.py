wordlist = ['banana', 'apple', 'orange']

# TODO 1 Randomly select a word from the wordlist and display its length

import random
selected_word = random.choice(wordlist)
length_of_word = len(selected_word)
word_to_guess = '_' * length_of_word
print(f'The word to guess is: {word_to_guess}\n')



# TODO 3 Check if the guessed letter is in the word
# TODO 7 we create a while loop to allow multiple guesses, user have 7 tries to guess the word
tries = 7
while tries > 0 and '_' in word_to_guess:
    # TODO 2 Ask the user to guess a letter
    guessed_letter = input("Guess a letter: ").lower()  # Przeniesiono do wnętrza pętli
    if guessed_letter in selected_word:
        print(f"Good job! The letter '{guessed_letter}' is in the word.\n")
        # TODO 4 Update the word_to_guess with the correct letter and print the updated word
        word_to_guess = ''.join(
            [guessed_letter if selected_word[i] == guessed_letter else word_to_guess[i] for i in range(length_of_word)]
        )
        print(f"Updated word: {word_to_guess}")
    else:
        print(f"Sorry, the letter '{guessed_letter}' is not in the word.\n")
        # TODO 5 Print the current state of the word_to_guess
        print(f"Current word: {word_to_guess}")
        # TODO 6 Decrease the number of tries left
        tries -= 1
        print(f"You have {tries} tries left.")