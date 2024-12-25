import random

def ComputersNumber(xTop):
    """
    computer selects a random number for the user to guess
    :param xTop: top of range of selected number (inserted by user)
    :return: computer's number
    """
    computersNum = random.randint(1, int(xTop))
    print(f"Computer thought of a number between 1 and {xTop}")
    return computersNum

def GuessingNumber(compNum, userNum, xTop):
    """
    itterate guesses until success
    :param compNum: random number computer guessed
    :param userNum: first number the user guessed
    :param xTop: top range of numbers
    :return:
    """
    num = 0
    while compNum != userNum:
        if compNum < userNum:
            print("Sorry, your number is too high")
        elif compNum > userNum:
            print("Sorry, your number is too low")
        userNum = int(input(f"Try again: Guess the number Computer thought of between 1 to {xTop}: "))
        num += 1
    print(f"Yeah! you guessed the number in {num+1} guesses")

def start():
    xTop = input("\n\nGuess the number the computer is thinking of!\nSelect the top range of the number: ")
    randNum = ComputersNumber(xTop)
    users1Guess = input(f"Guess the number Computer thought of between 1 to {xTop}: ")
    GuessingNumber(int(randNum), int(users1Guess), int(xTop))


