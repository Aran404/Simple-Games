# Rock Paper Scissors against a computer
import random

def game():

    computerscore = 0
    userscore = 0

    chars = "rps"

    attempts = int(input("What do you want to play to?: "))

    while attempts > computerscore + userscore:
            computer = random.choice(chars)

            user = str(input("What are you picking rock (r) paper (p) or scissors (s): "))
            user.lower()    

            if computer == user:
                print("Draw Game")
            elif computer == 'r' and user == 's':
                print("Computer wins")
                computerscore += 1
            elif computer == 's' and user == 'p':
                print("Computer wins")
                computerscore += 1
            elif computer == 'p' and user == 'r':
                print("Computer wins")
                computerscore += 1
            elif user == 's' and computer == 'p':
                print("User Wins")
                userscore += 1
            elif user == 'r' and computer == 's':
                print("User Wins")
                userscore += 1
            elif user == 'p' and computer == 'r':
                print("User Wins")
                userscore += 1
            print("You picked {} and the computer picked {}".format(user,computer))

            if computerscore < userscore:
                print("User = {}  Computer = {}".format(userscore,computerscore))
            elif computerscore == userscore:
                print("No Score was added")
            else:
                print("User = {} Computer = {}".format(userscore,computerscore))

    playagain = input("Do you want to play again? y or n: ")
    if playagain == 'y':
        game()
    elif playagain == 'n':
        exit()
    else:
        exit()

# 21 where you can only pick 1 or 2 and its gets added to the sum each time, if the sum = 21 or above you lose

def twenty():
    user = 0
    user1 = 0
    while user + user1 < 20:
        user2 = int(input("User 1, What number are you picking 1 or 2?: "))
        user += user2
        user3 = int(input("User 2, What number are you picking 1 or 2?: "))
        user1 += user3


        if user + user1 > 20:
            print("Game Over")



# Random number game

def func():
    computer = random.randint(1,10)
    i = 1
    while i > 0:
        user = int(input("Pick a number between 1 and 10: "))
        if user == computer:
            print("You are correct")
            i -= 1
        elif user > 10:
            print("The number has to be less then 10")
        elif user < computer:
            print("Higher")
        elif user > computer:
            print("Lower")
        elif i == 0:
            exit()
        else:
            print("error")


# To pick what game you want to play

choice = input("What game do you want to play? Rock Paper scissors (rps), 21(twenty) or random number (num)?: ").lower()

if choice == 'rps':
    game()
elif choice == 'num':
    func()
elif choice == 'twenty':
    twenty()
else:
    print("Error Game Not Found")
