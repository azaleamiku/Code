names = []
numn = int(input("How many names do you want?: "))

for n in range(numn):
    name = input("Name: ")
    names.append(name)

names.sort()

for name in names:
    print(name)