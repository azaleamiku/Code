password = ""

while password.lower() != "password":
    password = input("Enter Password: ")
    if password.lower() != "password":
        print("Incorrect. Try again.")

print("Access granted!")
