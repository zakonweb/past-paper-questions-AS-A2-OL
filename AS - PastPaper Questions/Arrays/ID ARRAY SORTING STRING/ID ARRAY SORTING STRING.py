UserNameArray = ["" for i in range(100)]

for i in range(100) :
    UID = input()
    UNAME = input()
    UserNameArray[i] = UID + UNAME

for j in range(98, -1, -1):
    alreadySorted = True
    print(j)
    for i in range(j):
        if UserNameArray[i][:6] > UserNameArray[i+1][:6]:
            t = UserNameArray[i]
            UserNameArray[i] = UserNameArray[i+1]
            UserNameArray[i+1] = t
            alreadySorted = False
    if alreadySorted: break