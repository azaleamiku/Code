while True:
    num1 = float(input("First Number: "))
    op = input("Operation (+, -, *, / or word): ").lower()
    num2 = float(input("Second Number: "))

    if op in ["addition", "+"]:
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif op in ["subtraction", "-"]:
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif op in ["multiplication", "*"]:
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif op in ["division", "/"]:
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid operation.")

    ask = input("Calculate again? [y]/[n] ").lower()
    if ask != "y":
        break
