"""
Question 3 
A program implements two stacks using 1D arrays. One stack stores the names of colours. One
stack stores the names of animals.
(a) The program contains the following global arrays and variables:
• 1D array Animal to store the names of up to 20 animals.
• 1D array Colour to store the names of up to 10 colours.
• AnimalTopPointer to point to the next free space in the array Animal, initialised to 0.
• ColourTopPointer to point to the next free space in the array Colour, initialised to 0.
Write program code to declare the global arrays and variables.
"""
# Global arrays and variables
Animal = ["" for i in range(20)]
Colour = ["" for i in range(10)]
AnimalTopPointer = 0
ColourTopPointer = 0

"""
(b) (i) Study the pseudocode function PushAnimal():
FUNCTION PushAnimal(DataToPush : STRING) RETURNS BOOLEAN
    IF AnimalTopPointer = 20 THEN
        ETURN FALSE
    ELSE
        Animal[AnimalTopPointer] DataToPush
        AnimalTopPointer AnimalTopPointer + 1
        RETURN TRUE
    ENDIF
ENDFUNCTION
Write program code for the function PushAnimal()
"""
# Function to push an animal onto the stack
def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True

"""
(ii) Study the pseudocode function PopAnimal():
FUNCTION PopAnimal() RETURNS STRING
    DECLARE ReturnData : STRING
    IF AnimalTopPointer = 0 THEN
        RETURN ""
    ELSE
        ReturnData ← Animal[AnimalTopPointer - 1]
        AnimalTopPointer ← AnimalTopPointer - 1
        RETURN ReturnData
    ENDIF
ENDFUNCTION
Write program code to declare the function PopAnimal()
"""
# Function to pop an animal from the stack
def PopAnimal():
    global AnimalTopPointer
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData

"""
(iii) The procedure ReadData():
• reads the animal names from the file AnimalData.txt
• uses PushAnimal() to insert each name onto the stack
• uses appropriate exception handling if the file does not exist.
Write program code for the procedure ReadData()
"""

# Procedure to read animal names from a file and push them onto the stack
"""
def ReadData():
    try: # Try to read from the file
        file = open("AnimalData.txt", "rt")
        for i in range(20):
            animal = file.readline().strip()
            if animal == "": # If the file ends before 20 animals are read, break
                break
            PushAnimal(animal)
        file.close()
    except: # Handle file not found or read error
        print("Error reading file or file not found.")
"""

"""
(iv) The function PushColour() performs the same actions as PushAnimal() but inserts
an item into Colour.
The function PopColour() performs the same actions as PopAnimal() but removes
the next item from Colour.
Write program code for the functions PushColour() and PopColour()
"""
# Function to push a colour onto the stack
def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True

# Function to pop a colour from the stack
def PopColour():
    global ColourTopPointer
    ReturnData = ""
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData

"""
(v) Amend the procedure ReadData() so that it also:
    • reads the colours from the text file ColourData.txt
    • uses PushColour() to insert each colour onto the stack
    • uses appropriate exception handling if the file does not exist.
"""
def ReadData():
    try: # Try to read from the animal file
        file = open("AnimalData.txt", "rt")
        for i in range(20):
            animal = file.readline().strip()
            if animal == "": # If the file ends before 20 animals are read, break
                break
            PushAnimal(animal)
        file.close()
    except: # Handle file not found or read error
        print("Error reading file or file not found.")

    try: # Try to read from the colour file
        file = open("ColourData.txt", "rt")
        for i in range(10):
            colour = file.readline().strip()
            if colour == "": # If the file ends before 10 colours are read, break
                break
            PushColour(colour)
        file.close()
    except: # Handle file not found or read error
        print("Error reading file or file not found.")

"""
(c) The procedure OutputItem():
• pops the next item from both Animal and Colour
• outputs the colour and animal on one line, for example "black horse" If there is no data in Colour:
• the animal is pushed back onto Animal
• "No colour" is output.
If there is no data in Animal:
• the colour is pushed back onto Colour
• "No animal" is output.
Write program code for the procedure OutputItem()
"""

# Procedure to output the next item from both stacks
def OutputItem():
    animal = PopAnimal()
    colour = PopColour()
    if colour == "": # If there is no colour, push the animal back and output "No colour"
        PushAnimal(animal)
        print("No colour")
    else:
        if animal == "":
            PushColour(colour)
            print("No animal")
        else:
            print(colour, animal) # Output the animal and colour, like "black horse"
    
"""
(d) The main program:
• calls the procedure ReadData()
• calls OutputItem() four times.
(i) Write program code for the main program.
"""
# Main program
ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()