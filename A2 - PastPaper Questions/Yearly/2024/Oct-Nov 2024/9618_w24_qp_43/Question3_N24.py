# Global variables
LinkedList = [[-1, -1] for _ in range(20)]  # 20 nodes, [Data, Pointer]
FirstEmpty = 0  # Free node pointer
FirstNode = -1  # List Header 

# Initialise pointer part of LinkedList
for i in range(19):
    LinkedList[i][1] = i + 1
LinkedList[19][1] = -1  # Last node points to -1 (end of empty list)

def InsertData():
    global LinkedList, FirstEmpty, FirstNode
    
    for _ in range(5):
        if FirstEmpty == -1:
            print("Linked list is full.")
        else:
            newData = int(input("Enter a positive integer: "))
            
            # Allocate a new node from the empty list
            NewNodeIndex = FirstEmpty
            FirstEmpty = LinkedList[NewNodeIndex][1]  # Move to next free node
            
            # Insert the data and link it to current list
            LinkedList[NewNodeIndex][0] = newData
            LinkedList[NewNodeIndex][1] = FirstNode  # Point to current first node
            
            # Update FirstNode to new node
            FirstNode = NewNodeIndex

def OutputLinkedList():
    global LinkedList, FirstNode
    current = FirstNode
    while current != -1:
        print(LinkedList[current][0])
        current = LinkedList[current][1]


# RemoveData procedure to remove a node with a given value
def RemoveData(value):
    global LinkedList, FirstNode, FirstEmpty

    current = FirstNode
    previous = -1

    # Traverse the list to find the node with the given value
    while current != -1:
        if LinkedList[current][0] == value:
            # Found the node to remove
            if previous == -1:
                # Removing the first node
                FirstNode = LinkedList[current][1]
            else:
                # Link the previous node to the next node
                LinkedList[previous][1] = LinkedList[current][1]

            # Add the node back to the free list
            LinkedList[current][0] = -1
            LinkedList[current][1] = FirstEmpty
            FirstEmpty = current
            return
        previous = current
        current = LinkedList[current][1]


# main program
InsertData()
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()
