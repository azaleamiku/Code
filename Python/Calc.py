def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def mod(x, y):
    return x % y

while True:
    try:
        x = int(input("First number: "))
        y = int(input("Second number: "))
        op = input("Select your Operation (add, sub, mul, div, mod): ")

        if op == "add":
            print(add(x, y))
        elif op == "sub":
            print(sub(x, y))
        elif op == "mul":
            print(mul(x, y))
        elif op == "div":
            print(div(x, y))
        elif op == "mod":
            print(mod(x, y))
        else:
            print("Invalid operation.")
    except:
        print("Invalid input, try again.")
        continue

    q = input("Do you want to try again? [y] or [n]? ").lower()
    if q == "n":
        break
