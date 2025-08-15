for i in range(1, 6):
    print(i * "*")
    
total = 1

for x in range(1, 101):
    total += x
print("The total is", total)

count = 10

while count > 0:
    print("Countdown...", count)
    count -= 1

for i in range(3):
    name = input("What's your name? ")
print("Yo,", name)

times = int(input("Give me a number to multiply: "))

for i in range (11):
    print(times, "x", i, "=", times * i)
