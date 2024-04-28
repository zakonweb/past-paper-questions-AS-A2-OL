'''
A linear queue is implemented using the 1D array, Queue. The index of the first element in the
array is 0.
(a) (i) Write program code to declare:
• Queue — a global array with space to store 50 IDs of type string
• HeadPointer — a global variable to point to the first element in the queue,
initialised to -1
• TailPointer — a global variable to point to the next available space in the queue,
initialised to 0
'''
# declare global variables
# Queue - a global array with space to store 50 IDs of type string
Queue = [None for i in range(50)]

# HeadPointer - a global variable to point to the first element in the queue, initialised to -1
HeadPointer = -1 # elements are removed from the head

# TailPointer - a global variable to point to the next available space in the queue, initialised to 0
TailPointer = 0 # elements are added at the tail

'''
(ii) The procedure Enqueue() takes a string parameter.
If the queue is full, the procedure outputs a suitable message. If the queue is not full, the
procedure inserts the parameter into the queue and updates the relevant pointer(s).
Write program code for Enqueue().
'''
# procedure Enqueue() takes a string parameter
def Enqueue(ID): # Adding an element to the LINEAR queue
    global TailPointer, HeadPointer
    # queue is full, that is all elements added are removed
    if TailPointer == 49: 
        print("Queue is full...")
    else:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = ID
        TailPointer += 1

'''
(iii) The function Dequeue() checks if the queue is empty.
If the queue is empty, the function outputs a suitable message and returns the string "Empty".
If the queue is not empty, the function returns the first element in the queue and updates the relevant pointer(s).

Write program code for Dequeue().
'''
# function Dequeue() checks if the queue is empty
def Dequeue(): # Removing an element from the LINEAR queue
    global HeadPointer

    # Check if the queue is empty
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("The queue is empty.")
        return "Empty"
    else:
        # Retrieve the first element in the queue
        firstElement = Queue[HeadPointer]
        
        # Update HeadPointer to the next element
        HeadPointer += 1

        # If the queue has become empty after dequeuing, reset pointers
        # This is not required by the question, but is a good practice
        # if HeadPointer == TailPointer:
        #    HeadPointer = -1
        #    TailPointer = 0

        return firstElement

'''
(b) A shop sells computer games. Each game has a unique identifier (ID) of string data type.
The text file QueueData.txt contains a list of game IDs.
The procedure ReadData() reads the data from the text file and inserts each item of data into the array Queue.

Write program code for the procedure ReadData().
'''
def ReadData():
    global TailPointer
    # with open("QueueData.txt", "rt") as file:
    file = open("QueueData.txt", "rt")
    for line in file:
        Enqueue(line.strip())
    file.close()

'''
(c) Some game IDs appear in the text file more than once.
The program needs to total the number of times each game ID appears in the text file.
The record structure RecordData has the following fields:
    • ID — a string to store the game ID
    • Total — an integer to store the total number of times that game ID appears in the text file.
(i) Write program code to declare the record structure RecordData.

If you are writing in Python, include attribute declarations as comments.
'''

# declare record structure RecordData
class RecordData: # RecordData is a UDT
    # DECLARE ID : STRING
    # DECLARE Total : INTEGER
    def __init__(self):
        self.ID = "" # a string to store the game ID
        self.Total = 0 # an integer to store the total number of times that game ID appears in the text file

'''
(ii) The global 1D array Records stores up to 50 items of type RecordData.
The global variable NumberRecords stores the number of records currently in the array Records and is initialised to 0.
Write program code to declare Records and NumberRecords.

If you are writing in Python, include attribute declarations as comments.
'''

# declare global variables
# Records - a global 1D array storing up to 50 items of type RecordData
Records = [RecordData() for i in range(50)]

# NumberRecords - a global variable storing the number of records currently in the array Records
NumberRecords = 0

'''
(iii) The pseudocode algorithm for the procedure TotalData():
• uses Dequeue() to remove an ID from the queue
• checks whether a RecordData with the returned ID exists in Records
• increments the total for that ID in the record if the ID already exists
• creates a new record and stores it in Records if the ID does not exist.
PROCEDURE TotalData()
    DECLARE DataAccessed : STRING
    DECLARE Flag : BOOLEAN
    DataAccessed ← Dequeue()
    Flag ← FALSE
    IF NumberRecords = 0 THEN
        Records[NumberRecords].ID ← DataAccessed
        Records[NumberRecords].Total ← 1
        Flag ← TRUE
        NumberRecords ← NumberRecords + 1
    ELSE
        FOR X ← 0 TO NumberRecords - 1
            IF Records[X].ID = DataAccessed THEN
                Records[X].Total ← Records[X].Total + 1
                Flag ← TRUE
            ENDIF
        NEXT X
    ENDIF
    IF Flag = FALSE THEN
        Records[NumberRecords].ID ← DataAccessed
        Records[NumberRecords].Total ← 1
        NumberRecords ← NumberRecords + 1
    ENDIF
ENDPROCEDURE
Write program code for the procedure TotalData().
'''
# procedure TotalData()
def TotalData():
    global NumberRecords
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords += 1
    else:
        for X in range(NumberRecords):
            if Records[X].ID == DataAccessed:
                Records[X].Total += 1
                Flag = True
    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords += 1

'''
(d) The procedure OutputRecords() outputs the ID and total of each record in Records in the format using the following format in f string:
ID 1234 Total 4
Write program code for OutputRecords().
'''
def OutputRecords():
    for i in range(NumberRecords):
        print(f"ID {Records[i].ID} Total {Records[i].Total}")

# Test the functions
'''
(e) The main program needs to:
• call ReadData()
• call TotalData() for each element in the queue
• call OutputRecords().
(i) Write program code for the main program.
'''

# read data from the text file and insert each item of data into the array Queue
ReadData() 

# call TotalData() for each element in the queue
while HeadPointer != TailPointer:
    TotalData()

# output the ID and total of each record in Records
OutputRecords()
