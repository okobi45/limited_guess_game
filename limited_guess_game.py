import random
import time

#This runs the intro 

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print()
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Set the maximum number of attempts
    
    while attempts < max_attempts:
        print(f"You have {max_attempts - attempts} attempts left.")
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            print("Let's celebrate!")
            celebrate()
            break

    if attempts >= max_attempts:
        print("Game over! You've used all your attempts.")
        print("The secret number was:", secret_number)

def celebrate():
    for _ in range(3):
        print("✨🎉✨🎉✨🎉")
        time.sleep(1)

guess_the_number()
