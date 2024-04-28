'''
The  text  file  IntegerData.txt  stores  100  integer  numbers  between  1  and  100  inclusive.  A  
program is required to read in this data and perform searching and sorting on the data.
'''

'''
(a) Write  program  code  to  declare  a  global  1D  array,  DataArray,  with  space  for  100  integer values.
'''
DataArray = [0 for i in range(100)]

'''
(b) The procedure ReadFile() must read in the numbers from the text file and store each one in the array. Use appropriate exception handling.
Write program code for the procedure ReadFile().
'''

def ReadFile():
    try:
        file = open("IntegerData.txt", "rt")
        for i in range(100):
            DataArray[i] = int(file.readline())
        file.close()
    except:
        print("Error accessing file...")

'''
(c) The  function  FindValues()  asks  the  user  to  enter  a  number  to  search  for  in  the  array.  
The number input must be a whole number between 1 and 100 inclusive. The function then 
returns the number of times the number input appears in the array.

Write program code for the function FindValues().
'''
def FindValues():
    count = 0
    num = int(input("Enter a number to search for: "))
    while num < 1 or num > 100: # check if number is between 1 and 100; range check validation
        print("Invalid number")
        num = int(input("Enter a number to search for: "))
    
    for i in range(100):
        if DataArray[i] == num:
            count += 1
    return count

'''
(d) (i)  Write program code to call ReadFile() and FindValues() from the main program. 
The return value from FindValues() must be output with an appropriate message.

ReadFile()
x = FindValues()
print(f"The number appears {x} times in the array.")
'''

'''
(e) The  procedure  BubbleSort()  needs  to  perform  a  bubble  sort  on  the  array  and  print  the  contents of the sorted array.
  Write program code for the procedure BubbleSort() and call it from the main program.
'''
def BubbleSort():
    for i in range(100):
        for j in range(0, 100-i-1):
            if DataArray[j] > DataArray[j+1]:
                DataArray[j], DataArray[j+1] = DataArray[j+1], DataArray[j]
    
    print("Sorted Array:")
    for i in range(100):
        print(DataArray[i])

ReadFile()
BubbleSort()
