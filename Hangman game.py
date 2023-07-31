import random
from Words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word {"H", "E", "L", "L", "O"}
    alphabet = set(string.ascii_uppercase)  # {"A", "B", "C" ...}
    used_letters = set()  # what the user has guessed { "K", "L" ...}
    lives = 5

    # getting user input
    # Exit the while loop when Word_Letters are 0 or when lives are 0.
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a','b','cd']) --> 'a b cd'
        print('You have ', lives, ' Lives. You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        # Return Letter if Letter is in the set/list of used_letters, otherwise return "_" for in stead of the letter
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # User Input Letter, If the user letter is vaild, add it to the list of used letters.
        # If the user letter is in the word letter, clear the user_letter input. Otherwise, subtract a life
        # If the user uses the same letter, indicate it, Otherwise indicate a unknown character
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in the word')

        elif user_letter in used_letters:
            print('You have already user that character. Please try again.')

        else:
            print('Invalid Character')

    # gets here when len(word_letters) == 0 OR when lives == 0
    # If Lives are equal to 0, you lose, Otherwise you win.
    if lives == 0:
        print('You died, sorry.')
    else:
        print('You guessed the word', word, '!!')


hangman()
