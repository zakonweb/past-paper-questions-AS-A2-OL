NewString = "0"
Selected = 0

InString = input("Enter New String: ")

for Index in InString:
    if Index < "0" or Index > "9":
        NewValue = int(NewString)

        if NewValue > Selected:
            Selected = NewValue
            print(Selected)
        NewString = "0"
    else:
        NewString = NewString + Index
print(Selected)