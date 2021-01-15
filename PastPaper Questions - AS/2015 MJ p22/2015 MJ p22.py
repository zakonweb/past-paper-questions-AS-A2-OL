hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes"))
seconds = int(input("Enter seconds: "))
personalBest = int(input("Enter personal best: "))

seconds = seconds + (hours*60*60) + (minutes*60)
print("Race time in seconds:", seconds)

if seconds == personalBest:
    print("Equals personal best time")
elif seconds < personalBest:
    print("Personal best time is unchanged")
elif seconds > personalBest:
    print("New personal best time")

"""import sys


i = 3
NoOfAttempts = 0
Choice = 0
DisplayMenu()
while not 1<=Choice<=4 or NoOfAttempts == i:
    Choice = int(input("Enter choice (1..4)"))
    NoOfAttempts = NoOfAttempts + 1

if Choice == 1:
    ReadFile()
elif Choice == 2:
    print("Add customer code")
elif Choice == 3:
    print("Search customer code")
elif Choice == 4:
    sys.exit()"""