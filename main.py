import random as rdm
from word import words
import string


def get_valid_word(words):
    word = rdm.choice(words)

    while '-' in word or ' ' in word:
        word = rdm.choice(words)
    return  word.upper()

# print(get_valid_word(words))

def hangman():
    word = get_valid_word(words)
    #print(word)
    word_letters = set(word) #letters in the word
    print(word_letters)
    alphabet = set(string.ascii_uppercase)
    #print(alphabet)
    used_letters = set() #what the user has guessed
    lives = 6
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # used letters
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f"You have {lives} lives left. You\'ve used this letters: {' '.join(used_letters)}")

        # what current word is (ie  W - R D)
        word_list = [letter if letter in used_letters else  "_" for letter in word]
        #print(word_list)
        print(f"Current word: {' '.join(word_list)}")

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 #takes away  a live if the guess letter is wrong
                print('Letter is not in the word')
        elif user_letter in used_letters:
            print("you\'ve already used that character")
        else:
            print('Invalid character')
    if lives == 0:
        print(f"You\'ve died. The word was {word}")
    else:
        print(f"You've guessed the word {word.upper()}!!!")


hangman()