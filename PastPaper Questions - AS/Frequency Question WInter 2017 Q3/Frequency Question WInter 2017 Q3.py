from random import randint


def TestRandom(Repetitions):
    frequency = [0 for i in range(10)]

    ExpFreq = Repetitions / 10
    print("Expected Frequency is", ExpFreq)

    for a in range(Repetitions):
        b = randint(0, 9)
        frequency[b] = frequency[b] + 1

    print("Number     Frequency    Difference")
    for a in range(10):
        print(a, "    ", frequency[a], "     ", ExpFreq - frequency[a])


TestRandom(200)