def ReadData():
    Colours = [] # local array
    try:
        with open("Data.txt", "rt") as File:
            Colours = File.read().splitlines()
        return Colours
    except:
        print("No file found")
        return Colours

def FormatArray(DataArray):
    OutputText = ""
    for x in range(len(DataArray)):  # OR: for item in DataArray:
        OutputText += DataArray[x] + " "
    return OutputText.strip()

def CompareStrings(First, Second):
    Count = 0
    while True:
        if First[Count] < Second[Count]:
            return 1
        elif First[Count] > Second[Count]:
            return 2
        else:
            Count += 1

def Bubble(DataArray):
    ArrayLength = len(DataArray)
    for x in range(ArrayLength - 1):
        wasSwapped = False
        for y in range(0, ArrayLength - x - 1):
            if CompareStrings(DataArray[y], DataArray[y + 1]) == 2:
                # Swap
                wasSwapped = True
                DataArray[y], DataArray[y + 1] = DataArray[y + 1], DataArray[y]
        if not wasSwapped:
            return DataArray
    return DataArray

# main program
Colours = ReadData()  # Call the function from 1a
print(FormatArray(Colours))
print('-' * 15)
BubbleSorted = Bubble(Colours)  # sort using bubble sort
print(FormatArray(BubbleSorted))  # format and print