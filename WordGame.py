#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    spot = word.find(letter)
    if spot >= 0:
        return True
    else:
        return False

    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    if word[spot] ==letter:
        return True
    else:
        return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback = ""
    for spot in range(5):
        letter = myGuess[spot]
        if inSpot(letter, word, spot):
            feedback = feedback + letter.upper()
        elif inWord(letter, word):
            feedback = feedback + letter.lower()
        else: 
            feedback = feedback + "*"

    return feedback


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess
    guessNum = 1
    feedback = ""
    while guessNum < 6 and feedback != todayWord.upper():
        guess = "aaaa"
        while guess not in wordList:
            guess = input("Enter a word: ")
        feedback = rateGuess(guess, todayWord)
        print(feedback)
        guessNum - guessNum + 1
    #Ask user for their guess
    #Give feedback using on their word:
    if feedback == todayWord.upper():
        print("You Win!")
    else:
        print("Sorry, todays word was " + todayWord + ".")




if __name__ == '__main__':
  main()
