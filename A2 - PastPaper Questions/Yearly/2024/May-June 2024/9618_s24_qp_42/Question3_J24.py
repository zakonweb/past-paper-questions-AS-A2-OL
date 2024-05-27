'''3 A program sorts an array of integers and searches the array for a particular value.
(a) The array of integers, NumberArray, stores the following data in the order given:
100 85 644 22 15 8 1
The array is declared and initialised local to the main program.
Write program code to declare and initialise the array.'''
NumberArray = [100, 85, 644, 22, 15, 8, 1]

'''(b) (i) The following recursive pseudocode function sorts the array into ascending order using
an insertion sort and returns the sorted array.
DECLARE LastItem : INTEGER
DECLARE CheckItem : INTEGER
DECLARE LoopAgain : BOOLEAN

FUNCTION RecursiveInsertion(IntegerArray : ARRAY[] OF INTEGER,
    NumberElements : INTEGER) RETURNS ARRAY[] OF INTEGER
    IF NumberElements <= 1 THEN
        RETURN IntegerArray
    ELSE
        CALL RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem <- IntegerArray[NumberElements - 1]
        CheckItem <- NumberElements - 2
    ENDIF
    LoopAgain <- TRUE
    IF CheckItem < 0 THEN
        LoopAgain <- FALSE
    ELSE
        IF IntegerArray[CheckItem] < LastItem THEN
            LoopAgain <- FALSE
        ENDIF
    ENDIF
    WHILE LoopAgain
        IntegerArray[CheckItem + 1] <- IntegerArray[CheckItem]
        CheckItem <- CheckItem - 1
        IF CheckItem < 0 THEN
            LoopAgain <- FALSE
        ELSE
            IF IntegerArray[CheckItem] < LastItem THEN
                LoopAgain <- FALSE
            ENDIF
        ENDIF
    ENDWHILE
    IntegerArray[CheckItem + 1] <- LastItem
    RETURN IntegerArray
ENDFUNCTION

Write the program code for the pseudocode function RecursiveInsertion().'''
# DECLARE LastItem : INTEGER
# DECLARE CheckItem : INTEGER
# DECLARE LoopAgain : BOOLEAN
def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2

        while CheckItem >= 0 and IntegerArray[CheckItem] > LastItem:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem -= 1

        IntegerArray[CheckItem + 1] = LastItem
        return IntegerArray

'''(c) The function RecursiveInsertion()can be changed to use iteration instead of recursion.
(i) Write program code for the function IterativeInsertion()to perform the same
processes as RecursiveInsertion()but using iteration instead of recursion.'''
def IterativeInsertion(IntegerArray):
    for i in range(1, len(IntegerArray)):
        LastItem = IntegerArray[i]
        CheckItem = i - 1

        while CheckItem >= 0 and IntegerArray[CheckItem] > LastItem:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem -= 1

        IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

'''(d) The recursive function BinarySearch()takes the parameters:
    • IntegerArray - an array of integers
    • First - the index of the first array element
    • Last - the index of the last array element
    • ToFind - an integer to search for in the array.
The function uses recursion to perform a binary search for ToFind in IntegerArray.
The function returns the index where ToFind is stored or returns -1 if ToFind is not in the array.
(i) Write program code for the recursive function BinarySearch().'''
def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    mid = (First + Last) // 2
    if IntegerArray[mid] == ToFind:
        return mid
    elif IntegerArray[mid] > ToFind:
        return BinarySearch(IntegerArray, First, mid - 1, ToFind)
    else:
        return BinarySearch(IntegerArray, mid + 1, Last, ToFind)

# main program
'''(ii) Amend the main program to:
    • call RecursiveInsertion()with the initialised array NumberArray and the number of elements as parameters
    • output the word 'Recursive'
    • output the content of the returned array.'''
sorted_array_recursive = RecursiveInsertion(NumberArray.copy(), len(NumberArray))
print("Recursive")
print(sorted_array_recursive)

'''(ii) Write program code to amend the main program to also:
    • call IterativeInsertion()with the original initialised array NumberArray
    • output the word 'iterative'
    • output the content of the returned array.'''
sorted_array_iterative = IterativeInsertion(NumberArray.copy())
print("Iterative")
print(sorted_array_iterative)

'''(ii) Write program code to amend the main program to:
    • call BinarySearch()with the sorted array and the integer 644 as the search value
    • output 'Not found' if 644 is not found in the array
    • output the index if 644 is found in the array.'''
search_value = 644
result_index = BinarySearch(sorted_array_iterative, 0, len(sorted_array_iterative) - 1, search_value)
if result_index == -1:
    print("Not found")
else:
    print(f"Index of {search_value}: {result_index}")

# End of code
# Zafar Ali Khan (the ZAK)
# GitHub: zakonweb