import sys

T = input()
T = T.lower()
alphabet = dict()

for alpha in T:
    if (not alphabet.get(alpha)):
        alphabet.setdefault(alpha,0)
    alphabet[alpha] += 1
    
trigger = 0
temp = 0
key_ = None
for key, value in alphabet.items():
    if value > temp:
        key_ = key
        temp = value
        trigger = 0
    elif value == temp:
        trigger = -1

print(key_.upper()) if trigger != -1 else print("?")