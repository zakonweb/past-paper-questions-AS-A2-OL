"""
1 A program reads data from a file and searches for specific data.
(a) The main program needs to read 25 integer data items from the text file Data.txt into a
local 1D array, DataArray. We will use try..catch to handle any exceptions that may occur.
(i) Write program code to declare the local array DataArray
"""
# Array declaration
DataArray = [0 for i in range(25)]

# (ii) Amend the main program to read the contents of Data.txt into DataArray
# Read data from file into DataArray
try:
    file = open("Data.txt", "rt")
    for i in range(25):
        DataArray[i] = int(file.readline())
    file.close()
except:
    print("Error reading file or file not found.")

"""
(b) (i) The procedure PrintArray() takes an integer array as a parameter and outputs the
contents of the array in the order they are stored.
The items are printed on the same line, for example:
10 4 5 13 25
Write program code for the procedure PrintArray()
"""
# Procedure to print array
def PrintArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

# (ii) Amend the main program to output the contents of DataArray using the procedure PrintArray()
# Print the array
# PrintArray(DataArray)

"""
(c) The function LinearSearch():
    • takes an integer array and integer search value as parameters
    • counts and returns the number of times the search value is found in the array.
Write program code for the function LinearSearch()
"""
# Function to search for a value in an array
def LinearSearch(arr, value):
    count = 0 # Counter for the number of times the value is found
    for i in range(len(arr)): # Linear search
        if arr[i] == value: # If the value is found, increment the counter
            count += 1
    return count

"""
(d) (i) Amend the main program to:
    • prompt the user to input a whole number between 0 and 100 inclusive
    • read and validate the input from the user
    • call LinearSearch() with DataArray and the validated input value
    • output the result in the format: The number 7 is found 2 times.
"""
# Prompt user for input within a range and validate the input
value = 0
while True: # Repeat until a valid input is entered
    value = int(input("Enter a whole number between 0 and 100 inclusive: "))
    if value >= 0 and value <= 100:
        break
    else:
        print("Invalid input. Please enter a whole number between 0 and 100 inclusive.")
return_value = LinearSearch(DataArray, value)
print(f"The number {value} is found {return_value} times.")

# (ii) Test your program by inputting the number 12.
# The number 12 is found 1 times.
