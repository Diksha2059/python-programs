import random

number = random.randint(1, 100)
guess = None
tries = 0

while guess != number:
    guess = int(input("Guess the number (1-100): "))
    tries += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {tries} tries.")
