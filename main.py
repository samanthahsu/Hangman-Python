# ok this is a hangman game.
import random

wordlist = ["conceive", "autonomy", "superior", "kettle", "enthusiasm"]

rand = random.randint(0, len(wordlist) - 1)
word = list(wordlist[rand])
display_string = list("".ljust(len(word), "_"))

print("This word has " + str(len(word)) + " letters")

max_guesses = 6
letter = ""
dead = False


def reveal_letter(display, actual_word, l):
    index = 0
    for c in actual_word:
        if l == c:
            display[index] = l
        index += 1
    return display


while not word == letter and max_guesses > 0:
    print(str(display_string))
    option = input("Enter 1 to guess a letter, 2 to guess the word: ")
    if option == "1":
        letter = input("Guess a letter: ")
        if letter in word:
            display_string = reveal_letter(display_string, word, letter)
            print(letter + " is in the word!")
        else:
            max_guesses -= 1
            print(letter + " is not in the word!")
            print("You have " + str(max_guesses) + " guesses left!")
            if max_guesses == 0:
                dead = True
    elif option == "2":
        answer = input("Guess the word: ")
        if list(answer) == word:
            break
        else:
            print("That's not it...")
            max_guesses -= 1

print("The word is: " + str(word))
if dead:
    print("You Lose!")
else:
    print("You Win!")
