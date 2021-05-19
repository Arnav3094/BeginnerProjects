import random

options = "\n\t1. 'r' for Rock.\n\t2. 'p' for Paper.\n\t3. 's' for Scissors\n\t4. 'q' for Quit"
welcomeMessage = '\nWelcome to Rock-Paper-Scissors!'
table = "Play area"

print(welcomeMessage)

def isWin(u, c):
    if (u =='r' and c == 's') or (u == 's' and c == 'p') or (u == 'p' and c == 'r'): 
        return True
    else:
        return False



def play(user):
    while user != 'q':
        while True:
            print(options)
            user = input(">>> ").lower()
            if user in ['r', 'p', 's','q']:
                break
            else:
                print("Invalid option entered")
                continue
        
        if user == 'q':
            print("Goodbye!")
            break;
        comp = random.choice(['r', 'p', 's'])
        if comp == user:
            print("It's a Tie")
        elif isWin(user,comp):
            print("You Win")
        else:
            print("You Lose")

user = 'lol'
play(user)