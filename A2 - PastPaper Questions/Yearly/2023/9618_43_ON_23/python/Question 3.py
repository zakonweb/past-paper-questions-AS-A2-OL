"""
3 A computer game is written using object-oriented programming.
The game has multiple characters that can move around the screen.
The class Character stores data about the characters. Each character has a name, a current X (horizontal) position and a current Y (vertical) position.

# Attributes
Name : STRING
stores the name of the character as a string

XPosition : INTEGER
stores the X position as an integer

YPosition : INTEGER
stores the Y position as an integer

# Methods
Constructor()
initialises Name, XPosition and YPosition to its parameter values

GetXPosition()
returns the X position

GetYPosition()
returns the Y position

SetXPosition()
adds the parameter to the Y position
validates that the new Y position is between 0 and 10000 inclusive

SetYPosition()
adds the parameter to the X position
validates that the new X position is between 0 and 10000 inclusive

Move()
takes a direction as a parameter and calls either
SetXPosition or SetYPosition with an integer value
"""

class Character:
    # Attributes will be private for encapsulation purpose
    # PRIVATE Name : STRING
    # PRIVATE XPosition : INTEGER
    # PRIVATE YPosition : INTEGER

    # Constructor # first method to be defined and executed
    def __init__(self, name, x, y):
        self.__Name = name
        self.__XPosition = x
        self.__YPosition = y
    
    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    '''
    The set methods SetXPosition() and SetYPosition() each take a value as a parameter and add this to the current X or Y position.
    If the new value exceeds 10000, it is limited to 10000.
    If the new value is below 0, it is limited to 0.
    Write program code for the set methods.
    '''
    def SetXPosition(self, x):
        self.__XPosition += x
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        
        if self.__XPosition < 0:
            self.__XPosition = 0
    
    def SetYPosition(self, y):
        self.__YPosition += y
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        
        if self.__YPosition < 0:
            self.__YPosition = 0
    
    '''
    The method Move() takes a string parameter: "up", "down", "left" or "right".
    The table shows the change each direction will make to the X or Y position.
    Use the appropriate method to change the position value.

    Direction   Value change
    up          Y position + 10
    down        Y position - 10
    left        X position - 10
    right       X position + 10
    '''
    def Move(self, direction):
        # up and down are for Y position
        # left and right are for X position

        if direction == "up":
            self.SetYPosition(10)
        elif direction == "down":
            self.SetYPosition(-10)
        elif direction == "left":
            self.SetXPosition(-10)
        elif direction == "right":
            self.SetXPosition(10)
'''
The class BikeCharacter inherits from the class Character.

Constructor()
takes Name, XPosition and YPosition as parameters
calls its parent class constructor with the appropriate values

Move() # Polymorphism
overrides the method Move() from the parent class by
changing either the X position or the Y position by 20 instead of 10
'''

class BikeCharacter(Character):
    # Constructor
    def __init__(self, name, x, y):
        super().__init__(name, x, y)
    
    # Polymorphism - overriding the method Move()
    def Move(self, direction):
        if direction == "up":
            self.SetYPosition(20)
        elif direction == "down":
            self.SetYPosition(-20)
        elif direction == "left":
            self.SetXPosition(-20)
        elif direction == "right":
            self.SetXPosition(20)

# main program
'''
Write program code to declare a new instance of Character with the identifier Jack.
The starting X position is 50 and the starting Y position is 50, the character's name is Jack.
'''
Jack = Character("Jack", 50, 50) # and object of class Character

'''
Write program code to declare a new instance of BikeCharacter with the identifier Karla.
The starting X position is 100, the starting Y position is 50 and the character's name is Karla.
'''
Karla = BikeCharacter("Karla", 100, 50) # and object of class BikeCharacter

'''
Write program code to:
• take as input which of the two characters the user would like to move
• take as input the direction the user would like the character to move
• call the appropriate method to move the character
• output the character's new X and Y position in an appropriate format, for example:
"Karla's new position is X = 100 Y = 200"
All inputs require appropriate prompts and must be validated.
'''

# input which of the two characters the user would like to move
character = input("Which character would you like to move? (Jack or Karla): ")

# validate the input, this validation is case sensitive and called case-sensitive validation
while character != "Jack" and character != "Karla":
    character = input("Invalid input! Which character would you like to move? (Jack or Karla): ")

# input the direction the user would like the character to move
direction = input("Which direction would you like the character to move? (up, down, left or right): ")

# validate the input
while direction != "up" and direction != "down" and direction != "left" and direction != "right":
    direction = input("Invalid input! Which direction would you like the character to move? (up, down, left or right): ")

# call the appropriate method to move the character
if character == "Jack":
    Jack.Move(direction)
    print(f"Jack's new position is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
else:
    Karla.Move(direction)
    print(f"Karla's new position is X = {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")

'''
Test your program twice with the following inputs.
Test 1: jack right
Test 2: karla down
'''
# End of question 3