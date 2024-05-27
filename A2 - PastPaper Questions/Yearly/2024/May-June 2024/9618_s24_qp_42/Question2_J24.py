'''2 A binary tree stores data in ascending order. For example:
                15
        8               19
    3       10
A computer program stores integers in a binary tree in ascending order. The program uses
Object-Oriented Programming (OOP).
The binary tree is stored as a 1D array of nodes. Each node contains a left pointer, a data value
and a right pointer.
The class Node stores the data about a node.

Node Class
Attributes:
PRIVATE LeftPointer : INTEGER   # stores the index of the node to the left in the binary tree
PrIVATE Data : INTEGER :        # stores the node's data
PRIVATE RightPointer : INTEGER  # stores the index of the node to the right in the binary tree

# Methods
Constructor()   # initialises Data to its parameter value, initialises LeftPointer and RightPointer to -1
GetLeft()       # returns the left pointer
GetRight()      # returns the right pointer
GetData()       # returns the data value
SetLeft()       # assigns the parameter to the left pointer
SetRight()      # assigns the parameter to the right pointer
SetData()       # assigns the parameter to the data

(a) (i) Write program code to declare the class Node and its constructor.
Do not declare the other methods.
Use the appropriate constructor for your programming language.
If you are writing in Python, include attribute declarations using comments.'''
class Node:
    # Attributes declarations with PRIVATE keyword
    # PRIVATE LeftPointer : INTEGER
    # PRIVATE Data : INTEGER
    # PRIVATE RightPointer : INTEGER

    def __init__(self, data):
        self.__LeftPointer = -1
        self.__Data = data
        self.__RightPointer = -1

    '''(ii) The get methods GetLeft(), GetRight()and GetData()each return the relevant attribute.
    Write program code for the three get methods.'''
    def GetLeft(self):
        return self.__LeftPointer

    def GetRight(self):
        return self.__RightPointer

    def GetData(self):
        return self.__Data

    '''(iii) The set methods SetLeft(), SetRight()and SetData()each take a parameter and
    then store this in the relevant attribute.
    Write program code for the three set methods.'''
    def SetLeft(self, left):
        self.__LeftPointer = left

    def SetRight(self, right):
        self.__RightPointer = right

    def SetData(self, data):
        self.__Data = data


'''(b) The class TreeClass stores the data about the binary tree.
TreeClass Class
PRIVATE Attributes:
PRIVATE Tree[0:19] : Node       # an array of 20 elements of type Node
PRIVATE FirstNode : INTEGER     # stores the index of the first node in the tree
PRIVATE NumberNodes : INTEGER   # stores the quantity of nodes in the tree

# Methods
Constructor()
initialises FirstNode to -1 and NumberNodes to 0
initialises each element in Tree to a Node object with the data value of -1

InsertNode()    # takes a Node object as a parameter, inserts it in the array and updates the pointer for its parent node
OutputTree()    # outputs the left pointer, data and right pointer of each node in Tree

Nodes cannot be deleted from this tree.
(i) Write program code to declare the class TreeClass and its constructor.
Do not declare the other methods.
Use the appropriate constructor for your programming language.
If you are writing in Python, include attribute declarations using comments.'''
class TreeClass:
    # Attributes declarations with PRIVATE keyword
    # PRIVATE Tree[0:19] : Node
    # PRIVATE FirstNode : INTEGER
    # PRIVATE NumberNodes : INTEGER

    def __init__(self):
        self.__Tree = [Node(-1) for _ in range(20)]
        self.__FirstNode = -1
        self.__NumberNodes = 0

    '''(ii) The method InsertNode()takes a Node object, NewNode, as a parameter and inserts
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
        • once the position is found, InsertNode()sets the left or right pointer of its parent node
        • increments NumberNodes.
    Write program code for InsertNode().'''
    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:  # First node
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            current_index = self.__FirstNode  # Start at the root
            while True:
                if NewNode.GetData() < self.__Tree[current_index].GetData():
                    left_pointer = self.__Tree[current_index].GetLeft()
                    if left_pointer == -1:
                        self.__Tree[current_index].SetLeft(self.__NumberNodes)
                        break
                    else:
                        current_index = left_pointer
                else:
                    right_pointer = self.__Tree[current_index].GetRight()
                    if right_pointer == -1:
                        self.__Tree[current_index].SetRight(self.__NumberNodes)
                        break
                    else:
                        current_index = right_pointer
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1

    '''(iii) The method OutputTree()outputs the left pointer, the data and the right pointer for
    each node that has been inserted into the tree. The outputs are in the order they are
    saved in the array.
    If there are no nodes in the array, the procedure outputs ‘No nodes’.
    Write program code for OutputTree().'''
    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            print(f'Node \tLeft \tData \tRight')
            for i in range(self.__NumberNodes):
                node = self.__Tree[i]
                print(f'{i} \t{node.GetLeft()} \t{node.GetData()} \t{node.GetRight()}')

'''(c) (i) The main program declares an instance of TreeClass with the identifier TheTree.
Write program code for the main program.'''
# main program
TheTree = TreeClass()

# Insert nodes as specified in the question
data_values = [10, 11, 5, 1, 20, 7, 15]
for value in data_values:
    new_node = Node(value)
    TheTree.InsertNode(new_node)

# Output the tree
TheTree.OutputTree()

# End of code
# Zafar Ali Khan (the ZAK)
# GitHub: zakonweb