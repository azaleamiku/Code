pwd = input("Enter a Password: ")
pwdl = len(pwd)
has_symbol = any(char in "!@#$%^&*()-_+=" for char in pwd)


strength = 0
if pwdl >= 8:
    strength += 1
if any(c.islower() for c in pwd) and any(c.isupper() for c in pwd):
    strength += 1
if any(c.isdigit() for c in pwd):
    strength += 1
if has_symbol:
    strength += 1

if strength == 4:
    print("Strong password!")
elif strength == 3:
    print("Decent, but could be stronger.")
else:
    print("Weak password. Consider improving it.")
