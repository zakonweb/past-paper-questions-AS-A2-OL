'''A binary tree consists of nodes. Each node has 3 integer values: a left pointer, data and a right 
pointer.
 The binary tree is stored using a global 2D array.
 The pseudocode declaration for the array is:
 DECLARE ArrayNodes : ARRAY[0:19, 0:2] OF INTEGER
 For example:
• ArrayNodes[0, 0] stores the left pointer for the first node.
• ArrayNodes[0, 1] stores the data for the first node.
• ArrayNodes[0, 2] stores the right pointer for the first node.
 -1 indicates a null pointer, or null data.
 (a) Write program code to:
• declare the global 2D array ArrayNodes
• initialise all 3 integer values to -1 for each node.
'''
# Declare the global 2D array ArrayNodes
ArrayNodes = [[-1, -1, -1] for i in range(20)]

'''
(b) The binary tree stores the following values:
Index Left pointer Data Right pointer
0       1           20      5
1       2           15      -1
2       -1          3       3
3       -1          9       4
4       -1          10      -1
5       -1          58      -1
6       -1          -1      -1
FreeNode stores the index of the first free element in the array, initialised to 6. 
RootPointer stores the index of the first node in the tree, initialised to 0.
Amend your program by writing program code to store the given data in ArrayNodes and 
initialise the free node and root node pointers.
'''

# Initialise the binary tree
ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]
ArrayNodes[6] = [-1, -1, -1]

# Initialise the free node and root node pointers
FreeNode = 6
RootPointer = 0

'''
(c) The following recursive pseudocode function searches the binary tree for a given value. If the 
value is found, the function must return the index of the value. If the value is not found, the 
function must return -1.
  The function is incomplete. There are four incomplete statements.
  FUNCTION SearchValue(Root : INTEGER, ValueToFind : INTEGER) RETURNS INTEGER
     IF Root = -1 THEN
        RETURN -1
     ELSE
       IF ArrayNodes[Root, 1] = ValueToFind THEN
          RETURN .......................................
       ELSE
          IF ArrayNodes[Root, 1] = -1 THEN
             RETURN -1
          ENDIF
       ENDIF
     ENDIF
     IF ArrayNodes[Root, 1] ....................................... ValueToFind THEN
        RETURN SearchValue(ArrayNodes[............, 0], ValueToFind)
     ENDIF
     IF ArrayNodes[Root, ............] < ValueToFind THEN
        RETURN SearchValue(ArrayNodes[Root, 2], ValueToFind)
     ENDIF
  ENDFUNCTION

  # Complete the function pseudocode
  FUNCTION SearchValue(Root : INTEGER, ValueToFind : INTEGER) RETURNS INTEGER
        IF Root = -1 THEN
            RETURN -1
        ELSE
        IF ArrayNodes[Root, 1] = ValueToFind THEN
            RETURN Root
        ELSE
            IF ArrayNodes[Root, 1] = -1 THEN
                RETURN -1
            ENDIF
        ENDIF
        ENDIF
        IF ArrayNodes[Root, 1] > ValueToFind THEN
            RETURN SearchValue(ArrayNodes[Root, 0], ValueToFind)
        ENDIF
        IF ArrayNodes[Root, 1] < ValueToFind THEN
            RETURN SearchValue(ArrayNodes[Root, 2], ValueToFind)
        ENDIF
  '''

# Write program code for the function SearchValue()
def SearchValue(Root, ValueToFind):
    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:
            return Root
        else:
            if ArrayNodes[Root][1] == -1:
                return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)

'''
(d) A post order traversal performs the following operation:
• visit the left node
• visit the right node
• output the root.
  For example, in the following tree, the output would be:  3 9 25 60 50 
                    50
            25              60
        3       9

  An outline of the PostOrder() procedure is:
• If left node is not empty, make a recursive call with the left node as the root.
• If right node is not empty, make a recursive call with the right node as the root.
• Output the current root node.
  The procedure PostOrder() takes the root node as a parameter.
  Write program code for the procedure PostOrder().         
'''
def PostOrder(Root):
    if ArrayNodes[Root][0] != -1:
        PostOrder(ArrayNodes[Root][0])
    if ArrayNodes[Root][2] != -1:
        PostOrder(ArrayNodes[Root][2])
    print(ArrayNodes[Root][1])

'''
(e) (i)  Amend the main program by writing program code to:
• call the function SearchValue() to find the position of the number 15 in the tree
• use the result from SearchValue() to output either the index of the value if found,  
or an appropriate message to state that the value was not found
• call the procedure PostOrder().
'''

# Call the function SearchValue() to find the position of the number 15 in the tree
position = SearchValue(RootPointer, 15)
if position != -1:
    print(f"The value 15 is found at index {position}.")
else:
    print("The value 15 is not found.")

# Call the procedure PostOrder()
PostOrder(RootPointer)