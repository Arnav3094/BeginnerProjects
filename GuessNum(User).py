# from random import randint as rand

def compGuess():
    print("\nThis Computer is very smart. You have to choose a number\nand choose the limits for the computer to guess in.\nThe Computer will guess the number")
    lower = int(input("\tEnter the lower limit: "))
    upper = int(input("\tEnter the upper limit: "))
    chosenNumber = int(input("What number do you want the computer to guess: "))

    tryCount = 0

    table = f"Computer's Guesses:\tTry count:\t\tYour Number: {chosenNumber}"
    print(table)

    guess = -1
    while (guess != chosenNumber) :
        range = upper - lower
        guess = lower + range//2
        tryCount += 1
        table = f"{guess}\t\t\t {tryCount}"
        print(table)
        if guess > chosenNumber:
            # Means that I've guessed too high. So lower the upper bound
            upper = guess
        if guess < chosenNumber:
            # Means that I've guessed too high. So increase the lower bound
            lower = guess
    print(f"The computer guessed your number ({chosenNumber}) in {tryCount} tries")

compGuess()