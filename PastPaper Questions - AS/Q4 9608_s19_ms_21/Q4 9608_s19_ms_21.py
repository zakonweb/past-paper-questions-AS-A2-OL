InString = "12 34 5  39"
AfterSpace = False
Space = " "
NewString = ""

for NextChar in InString:
    if AfterSpace:
        if NextChar != Space:
            NewString = NewString + NextChar
            AfterSpace = False
    else:
        NewString = NewString + NextChar
        if NextChar == Space:
            AfterSpace = True

print(NewString)