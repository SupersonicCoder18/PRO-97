import random

print("Number Guessing Game")
number = random.randint(1, 9)
chance = 0
print("Guess a number between 1 and 9")

while chance < 5:
    guess = int(input("Enter your guess:-"))
    if (guess == number):
        print("CONGRATULATIONS!!!! YOU WIN!!!!")
    elif (guess < number):
        print("The number you have entered is too low, try again")
    else:
        print("The number you have entered is too high, try again")
    chance += 1

if not chance < 5:
    print("YOU LOSE!!!! The number is ", number)