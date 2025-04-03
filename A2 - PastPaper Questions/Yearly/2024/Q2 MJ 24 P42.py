# 9618/42/M/J/24 Q2
class Node:
    # Attributes
    # PRIVATE LeftPointer : INTEGER
    # PRIVATE Data : INTEGER
    # PRIVATE RightPointer : INTEGER

    def __init__(self, value):
        self.__LeftPointer = -1
        self.__data = value
        self.__RightPointer = -1
    
    def GetLeft(self):
        return self.__LeftPointer
    
    def GetData(self):
        return self.__data
    
    def GetRight(self):
        return self.__RightPointer
    
    def SetLeft(self, LP):
        self.__LeftPointer = LP
    
    def SetData(self, value):
        self.__data = value
    
    def SetRight(self, RP):
        self.__RightPointer = RP

class TreeClass:
    # Attributes
    # PRIVATE Tree[0:19] : ARRAY OF Node()
    # PRIVATE FirstNode : INTEGER
    # PRIVATE NumberNodes : INTEGER

    def __init__(self):
        self.__FirstNode = -1
        self.__NumberNode = 0
        self.__Tree = []

        for i in range(20):
            thisNode = Node(-1)
            self.__Tree.append(thisNode)
    
    '''
    The method InsertNode()takes a Node object, NewNode, as a parameter and inserts
    it into the array Tree.
    InsertNode()first checks if the tree is empty.
    If the tree is empty, InsertNode():
    • stores NewNode in the array Tree at index NumberNodes
    • increments NumberNodes
    • stores 0 in FirstNode.
    If the tree is not empty, InsertNode():
    • stores NewNode in the array Tree at index NumberNodes
    • accesses the data in the array Tree at index FirstNode and compares it to the
    data in NewNode
    • repeatedly follows the pointers until the correct position for NewNode is found
    • once the position is found, InsertNode() sets the left or right pointer of its parent
    node
    • increments NumberNodes.
    Write program code for InsertNode().
    '''

    def InsertNode(self, NewNode):
        if self.__NumberNode == 0: # check if tree is empty
            self.__Tree[self.__NumberNode] = NewNode
            self.__NumberNode += 1
            self.__FirstNode = 0
        else:
            CurrentNode = self.__FirstNode
            while True:
                if NewNode.GetData() < self.__Tree[CurrentNode].GetData():
                    if self.__Tree[CurrentNode].GetLeft() == -1:
                        self.__Tree[self.__NumberNode] = NewNode
                        self.__Tree[CurrentNode].SetLeft(self.__NumberNode)
                        self.__NumberNode += 1
                        break
                    else:
                        CurrentNode = self.__Tree[CurrentNode].GetLeft()
                else:
                    if self.__Tree[CurrentNode].GetRight() == -1:
                        self.__Tree[self.__NumberNode] = NewNode
                        self.__Tree[CurrentNode].SetRight(self.__NumberNode)
                        self.__NumberNode += 1
                        break
                    else:
                        CurrentNode = self.__Tree[CurrentNode].GetRight()
    
    def OutputTree(self):
        if self.__FirstNode == -1:
            print("No nodes.")
        else:
            print(f"Index\tData\tLeft\tRight")
            for i in range(self.__NumberNode):
                print(f"{i}\t{self.__Tree[i].GetData()}\t{self.__Tree[i].GetLeft()}\t{self.__Tree[i].GetRight()}")

# Main Program
TheTree = TreeClass()
values = [10, 11, 5, 1, 20, 7, 15]
for data in values:
    NewNode = Node(data)
    TheTree.InsertNode(NewNode)
TheTree.OutputTree()