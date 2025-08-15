import random

secret = random.randint(1, 10)


while True:
    num = int(input("Guess the number I'm holding: "))

    if num == secret:
        print("Success")
        break
    elif num < secret:
        print("Too low!")
    else:
        print("Too high!")