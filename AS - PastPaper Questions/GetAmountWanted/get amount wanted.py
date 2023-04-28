def GetAmountWanted():
    myAns = True
    while myAns:
        myAns = False
        Amount = int(input())
        if Amount % 10 == 0:
            return Amount
        else:
            Amount = int(input("Not appropriate. Again? "))
            if not myAns:
                return -1
