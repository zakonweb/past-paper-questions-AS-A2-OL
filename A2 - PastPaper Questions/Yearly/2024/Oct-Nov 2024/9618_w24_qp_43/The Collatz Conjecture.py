
def collatz_conjecture(n):
    if n <= 0:
        print("Enter a positive integer.")
        return

    print("Collatz conjecture starting from", n, "is:")
    while n != 1:
        print(n, end=" → ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)

number = int(input("Enter a positive integer: "))
collatz_conjecture(number)