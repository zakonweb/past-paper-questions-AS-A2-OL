"""
2 A business sells a single product. Customers can purchase one or more of this product.
 Each sale has an ID and a quantity, for example "ABC" and 2
 The business needs a program to store the data about the sales in a circular queue data structure. 
 (a) Write program code to declare a record structure, SaleData, to store the data about each 
sale.
"""
# UDT Record Structure
class SaleData:
    def __init__(self):
        self.ID = ""
        self.quantity = 0

"""
(b) Write program code to:
• declare a global array, CircularQueue, of 5 items to store the sale records
• declare the global pointers Head and Tail
• declare the global variable NumberOfItems
• initialise all elements of the array CircularQueue to an empty record, where the ID is null ("") and quantity is -1
• initialise Head, Tail and NumberOfItems to 0
"""
# Global Variables
CircularQueue = [SaleData() for i in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0
for i in range(5):
    CircularQueue[i].ID = ""
    CircularQueue[i].quantity = -1

"""
(c) The function Enqueue():
• takes a new record as a parameter
• inserts the record in the circular queue at the element pointed to by Tail
• updates pointers and other variables as required
• returns -1 if the circular queue is full
• returns 1 if the record is stored successfully.
  Write program code for the function Enqueue().
"""
def Enqueue(newRecord):
    global Tail, NumberOfItems
    if NumberOfItems == 5:
        return -1
    CircularQueue[Tail] = newRecord
    Tail = (Tail + 1) % 5 # Circular Queue Logic for Tail to wrap around
    '''
    # Alternative Logic for Tail = (Tail + 1) % 5
    Tail += 1
    if Tail == 5:
        Tail = 0
    '''
    NumberOfItems += 1
    return 1

"""
(d) The function Dequeue():
• returns a null or empty record if the circular queue is empty
• returns the first record in the queue if the circular queue is not empty
• updates pointers and other variables as required.
Write program code for the function Dequeue().
"""
def Dequeue():
    global Head, NumberOfItems
    if NumberOfItems == 0:
        return SaleData()
    record = CircularQueue[Head]
    Head = (Head + 1) % 5 # Circular Queue Logic for Head to wrap around
    '''
    # Alternative Logic for Head = (Head + 1) % 5
    Head += 1
    if Head == 5:
        Head = 0
    '''
    NumberOfItems -= 1
    return record

"""
(e) The procedure EnterRecord():
• takes an ID and quantity as input and creates a sale record
• uses Enqueue() to insert the record in the circular queue
• outputs "Full" if the record was not inserted in the circular queue
• outputs "Stored" if the record was inserted in the circular queue.
Write program code for the procedure EnterRecord().
"""
def EnterRecord(ID, quantity):
    newRecord = SaleData()
    newRecord.ID = ID
    newRecord.quantity = quantity
    if Enqueue(newRecord) == -1:
        print("Full")
    else:
        print("Stored")

"""
(f) The following sale records need to be entered into the program:
ID  Quantity
ADF 10
OOP 1
BXW 5
XXZ 22
HQR 6
LLP 3
(i) Amend the main program to:
• use EnterRecord() to input the six records in the table
• use Dequeue() to remove one record
• output either the ID and quantity of the removed record, or an error message if the circular queue is empty
• use EnterRecord() to input the record with the ID "LLP" for a second time
• output the ID and quantity for all the records currently stored in the array CircularQueue.
Write program code to perform these tasks.
"""
EnterRecord("ADF", 10)
EnterRecord("OOP", 1)
EnterRecord("BXW", 5)
EnterRecord("XXZ", 22)
EnterRecord("HQR", 6)
EnterRecord("LLP", 3)

record = Dequeue()
if record.ID == "":
    print("Empty, No Record Removed")
else:
    print(f"Removed Record: {record.ID}, {record.quantity}")

EnterRecord("LLP", 3)

for i in range(5):
    print(f"Record {i+1}: {CircularQueue[i].ID}, {CircularQueue[i].quantity}")