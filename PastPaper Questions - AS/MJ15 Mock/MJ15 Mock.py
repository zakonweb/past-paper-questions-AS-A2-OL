Choice = 5
CS = 0
Physics = 0
Chemistry = 0
Maths = 0
while not Choice == 0:
    Choice = int(input("Please enter choice (CS 1, Physics 2, Chemistry 3, Maths 4 or 0 to stop) : "))
    if Choice == 1:
        CS = CS + 1
    elif Choice == 2:
        Physics = Physics + 1
    elif Choice == 3:
        Chemistry = Chemistry + 1
    elif Choice == 4:
        Maths = Maths + 1
print("Computer Science", CS)
print("Physics", Physics)
print("Chemistry", Chemistry)
print("Maths", Maths)