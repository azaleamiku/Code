name = input("What's your name? ")
byr = int(input("What's your birth year? "))  # Convert to int directly
cyr = 2025

age = cyr - byr

print(f"\nHi {name}, you are {age} years old.")
