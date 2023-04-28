from random import randint

c = 0
NoArr = [0 for i in range(10)]

for i in range(10):
    alreadyFound = True
    while alreadyFound:
        c = c + 1
        alreadyFound = False
        x = randint(1, 20)
        for j in range(i, -1, -1):
            if NoArr[j] == x: alreadyFound = True

    NoArr[i] = x

for i in range(10):
    print(NoArr[i])

print("Loop worked for", c, "times.")