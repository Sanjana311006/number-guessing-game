import random
num=random.randint(0,10)
#print(num)
print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 10")
while(1):
    guess=int(input("Enter your guess:"))
    if(guess<num):
        print("Too low! Try again")
    else:
        if(guess>num):
            print("Too high!Try again")
        else:
            if(guess==num):
                print("Correct!You guessed the number!")
                break
