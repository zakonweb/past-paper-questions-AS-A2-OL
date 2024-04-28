"""
Question 1
1 A 1D array needs to store the names of 10 animals.
 (a) Write program code to declare the global string array Animals to store 10 items.
"""
# Program code to declare the global string array Animals to store 10 items.
Animals = ["" for i in range(10)]

"""
(b) The main program needs to store the following animals in the array:
   horse
   lion
   rabbit
   mouse
   bird
   deer
   whale
   elephant
   kangaroo
   tiger
  Write program code to store these animal names in the array.
  The names must be in lower case and stored in the order given in the list
"""
# Program code to store the following animals in the array
Animals = ["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "elephant", "kangaroo", "tiger"]

"""
(c) The  following  pseudocode  procedure  sorts  the  array  into  a  descending  alphabetical  order using only the first character in each animal name.
  The function LENGTH(DataArray) returns the number of elements in the array DataArray.
  The function MID(String, Start, Quantity) returns Quantity number of characters from String starting at index Start. The first character in the string is index 0, for example:
   MID("tiger", 0, 2) will return "ti"

  There are four incomplete statements in the procedure.
  PROCEDURE SortDescending()
    DECLARE ArrayLength : INTEGER
    DECLARE Temp : STRING
    ArrayLength ← LENGTH(Animals)
    FOR X ← 0 TO ArrayLength - 1
      FOR Y ← .................. TO ArrayLength - X - 1
        IF MID(Animals[Y], 0, 1) < MID(Animals[..................], 0, 1) THEN
          Temp ← Animals[..................]
          Animals[Y] ← Animals[Y + 1]
          Animals[Y + 1] ←  ..................
        ENDIF
      NEXT Y
    NEXT X
  ENDPROCEDURE

  # completed (blanks are filled in with the correct code) code
  PROCEDURE SortDescending()
    DECLARE ArrayLength : INTEGER
    DECLARE Temp : STRING
    ArrayLength ← LENGTH(Animals)
    FOR X ← 0 TO ArrayLength - 1
        FOR Y ← 0 TO ArrayLength - X - 1
            IF MID(Animals[Y], 0, 1) < MID(Animals[Y + 1], 0, 1) THEN
                Temp ← Animals[Y]
                Animals[Y] ← Animals[Y + 1]
                Animals[Y + 1] ← Temp
            ENDIF
        NEXT Y
    NEXT X
 ENDPROCEDURE
 Write program code for the procedure SortDescending().
"""
def SortDescending(): # Standard Bubble Sort Algorithm
    ArrayLength = len(Animals)
    for X in range(ArrayLength - 1):
        for Y in range(ArrayLength - X - 1):
            if Animals[Y][0] < Animals[Y + 1][0]: # < because we want to sort in descending order
                Temp = Animals[Y]
                Animals[Y] = Animals[Y + 1]
                Animals[Y + 1] = Temp


"""
(d) (i)  Write program code to amend the main program to:
• call the procedure SortDescending()
• output the sorted contents of the array with each animal name on a new line.
"""
SortDescending()
for animal in Animals:
    print(animal)