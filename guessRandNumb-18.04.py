import random 
import keyboard
import sys
found = False
correctNumber = random.randint(1, 100)
attempts = 0
def welc(attempts):
    if attempts == 0:
        print("\nThis is a game where you guess the number between 1 and 100\nanything above 100 will exit the program\n\n")


def get_guess():
    while found == False: 
        try:
            welc(attempts)
            guess = int(input("Please enter a number:\n"))
            print(f"guess: {guess}")
            return guess
        except ValueError:
            print("NaN - Please enter a valid number\n")

def evaluate_guess(guess):
    global found 
    if guess == correctNumber:
        found = True
        print("You guessed the correct number")
    elif guess > 100 or guess < 0:
        sys.exit("Exiting.")
    elif guess < correctNumber:
        print("Too low\n")
    else:
        print("Too high\n")
        

while True:
    if found == True:
        print(f"you did it in: {attempts} attempts")
        break
    else:
        evaluate_guess(get_guess())
    attempts = attempts + 1

while True:
    if keyboard.is_pressed('q'):
        print("Exiting")
        sys.exit("Exiting Program")