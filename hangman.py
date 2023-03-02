import getpass
hangman = ["______", "|    |", "|    |",
           "|    O", "|   \|/", "|    |", "|   / \\", " "]


word = getpass.getpass("Enter the word: ")
wordList = []
word = word.lower()
for char in word:
    wordList.append(char)

matched = 0
life = 0


def takeGuess():
    global life
    global matched
    guess = input("Enter the guessed word: ")
    guess = guess.lower()

    if guess in wordList or matched == len(word):
        if matched == len(word):
            print("You Lost")
            return
        else:
            print(" ")
            wordList.remove(guess)
            print("Enter the next letter")
            matched += 0
            print(matched)
            takeGuess()

    else:
        for i in range(life):
            if life == 7:
                [print(x) for x in hangman]
                print("")
                print("You Lost")
                return
                break
            else:
                print(hangman[i])
        print("")
        print("")
        print("Wrong guess! \n {} attempts left \n".format(7-life))
        life += 1
        takeGuess()


takeGuess()

print(" ")
print("The word is: ", word)
print(" ")
print(" Game Ended")
