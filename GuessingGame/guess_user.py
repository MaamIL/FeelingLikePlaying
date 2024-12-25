import random

def GuessingNumber(xLow, xTop):
    """
    itterate guesses until success
    :param xLow: low range of numbers to guess (1)
    :param xTop: high range of numbers to guess (inserted by user)
    """
    compGuess = random.randint(xLow, int(xTop))
    num = 0
    userFeedBack = ""
    while userFeedBack != "e":  #while its not equal- the computer didn't guess yet
        num += 1
        userFeedBack = input(f"Computer guesses {compGuess}. Is the guess higher (h) / lower (l) / equal (e) your number? ")
        if userFeedBack == "h":  #if the guess is higher- it turns to be the new top range
            xTop = compGuess
        elif userFeedBack == "l": #if the guess is lower- it turns to be the new bottom range
            xLow = compGuess
        elif userFeedBack != "e": #if the input is other than h/l/e
            print("You are waisting my guesses...")
        compGuess = random.randint(xLow, int(xTop))
    print(f"Yeah! Computer guessed your number in {num} guesses")

def start():
    xTop = input("\n\nThe computer will guess the number you are thinking of!\nSelect the top range of the number: ")
    print("Now, think of a number between 1 and " + xTop)
    GuessingNumber(1, xTop)



