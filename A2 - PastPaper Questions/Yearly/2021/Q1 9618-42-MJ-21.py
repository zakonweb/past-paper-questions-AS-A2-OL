# Q1 9618/42/M/J/21
class node:
    def __init__(self):
        self.data = 0
        self.nextNode = 0

linkedList = [node() for _ in range(10)]
startPointer = 0
emptyList = 5

def outputNode(linkedList, startPointer):
    currPtr = startPointer
    while currPtr != -1:
        print(linkedList[currPtr].data, end = ' ')
        currPtr = linkedList[currPtr].nextNode

def addNode(linkedList, emptyList, startPointer):
    if emptyList == -1:
        # print("Overflow. List is full...")
        return linkedList, emptyList, False
    else:
        item = int(input("Enter item to add to the LL: "))
        newPtr = emptyList
        linkedList[newPtr].data = item
        emptyList = linkedList[emptyList].nextNode
        currPtr = startPointer
        prev = -1
        while currPtr != -1:
            prev = currPtr
            currPtr = linkedList[currPtr].nextNode
        linkedList[prev].nextNode = newPtr
        linkedList[newPtr].nextNode = -1        
        return linkedList, emptyList, True

# main program
linkedList[0].data = 1
linkedList[0].nextNode = 1
linkedList[1].data = 5
linkedList[1].nextNode = 4
linkedList[2].data = 6
linkedList[2].nextNode = 7
linkedList[3].data = 7
linkedList[3].nextNode = -1
linkedList[4].data = 2
linkedList[4].nextNode = 2
linkedList[5].data = 0
linkedList[5].nextNode = 6
linkedList[6].data = 0
linkedList[6].nextNode = 8
linkedList[7].data = 56
linkedList[7].nextNode = 3
linkedList[8].data = 0
linkedList[8].nextNode = 9
linkedList[9].data = 0
linkedList[9].nextNode = -1

outputNode(linkedList,startPointer)
print()
print()
linkedList, emptyList, status = addNode(linkedList,emptyList, startPointer)
outputNode(linkedList,startPointer)
if not status:
    print("Overflow occured...")
else:
    print("Addition to the LL is successful!!!")
