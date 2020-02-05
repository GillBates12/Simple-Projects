lives = 7
stringword= "Litty"
word = list("Litty".lower())
guess = ["_"] * len(word)
winner = False
incorrectLetters = []

def printscore():
    print("\n\nLives: " + str(lives))
    print("Incorrect letters:", end="")
    for x in range(len(incorrectLetters)):
        if x == len(incorrectLetters) - 1:
            print(incorrectLetters[x], end="")
        else:
            print(incorrectLetters[x], end=",")
    print("")
    for x in range(len(guess)):
        if x == len(guess) - 1:
            print(guess[x], end="")
        else:
            print(guess[x], end=",")
    print("")

def guessletter():
    letterguess = (input("Guess a letter: ")).lower()
    correct = False
    for x in range(len(word)):
        if letterguess == word[x]:
            guess[x] = letterguess
            correct = True
    if correct:
        print("Your guess was correct!")

    else:
        print("Your guess was incorrect!")
        incorrectLetters.append(letterguess)
        global lives
        lives -= 1

def checkwinner():
    if "_" not in guess:
        global winner
        winner = True




while lives > 0 and winner == False:

    printscore()
    guessletter()
    checkwinner()

if lives <= 0:
    print("Sorry you lost. The word was " + stringword)
else:
    print("You won with " + str(lives) + "" + "lives left")










