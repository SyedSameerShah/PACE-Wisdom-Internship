import random
import string

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '_' in word or ' ' in word:
        word = random.choice(word_list)
    return word

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","acceptable","accessible","accidental","accurate","acid","acidic","acoustic","acrid","actually","ad hoc"]

    word = get_valid_word(words)
    word_characters = set(word)
    valid_characters = set(string.ascii_uppercase)
    guessed_letters = set()

    lives = 10

    while word_characters and lives > 0:
        print(f"You have {lives} lives left and you have used these letters: {' '.join(guessed_letters)}")
        print("Current word:", display_word(word, guessed_letters))

        user_input = input("Guess a letter: ").lower()

        if user_input in valid_characters - guessed_letters:
            guessed_letters.add(user_input)
            if user_input in word_characters:
                word_characters.remove(user_input)
            else:
                lives -= 1
                print("Letter is not in word")

        elif user_input in guessed_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid input. Please enter a single letter.")

    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, "!!")

hangman()