# Number-guessing-game-
#The program choose a number between 1 to 100.
import random

n = random.randint(1, 100)
guess = int(input("Enter your guess (1 to 100): "))
#user guess untill it's correct 
if guess > n:
    print("Too High!")
#after each guesses program will check the possibility of the condition
elif guess < n:
    print("Too Low!")
#the number is guessed
else:
    print("You guessed right!", n)
