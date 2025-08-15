import random

secret = random.randint(1, 20)
attempts = 0

while True: 
    num = int(input("Guess the number from 1 to 20: "))
    attempts += 1

    if num == secret:
        print("Correct! You guessed it in", attempts, "tries.")
        break
    elif num < secret:
        print("Too low!")
    else:
        print("Too high!")
