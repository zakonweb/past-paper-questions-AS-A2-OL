UserNameArray = ["" for i in range(100)]

for j in range(98, -1, -1):
    alreadySorted = True
    for i in range(j):
        CurrentID = UserNameArray[i][:6]
        NextID = UserNameArray[i+1][:6]

        if CurrentID > NextID:
            t = UserNameArray[i]
            UserNameArray[i] = UserNameArray[i+1]
            UserNameArray[i+1] = t
            alreadySorted = False
    if alreadySorted: break