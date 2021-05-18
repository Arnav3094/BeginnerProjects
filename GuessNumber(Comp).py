from random import randint as r

x = 10

welcomeMessage = f"\nHello!\nWe have chosen a number between one and {x}, which\nyou have to guess!\n"

def guess():
    print(welcomeMessage)
    randNum = r(0, x+1)
    guess = -1
    while (guess != randNum):
        guess = int(input("> "))
        if guess > randNum:
            print("Your guess is too high, guess lower!")
        elif guess < randNum:
            print("Your guess is too low, guess higher!")
    print("YAY, you guessed it!")
    
guess()