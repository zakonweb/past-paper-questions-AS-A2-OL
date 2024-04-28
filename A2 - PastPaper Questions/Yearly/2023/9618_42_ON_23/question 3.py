"""
A computer game is written using object-oriented programming.
The game has multiple characters.
The class Character stores data about the game characters. Each character has a name, date
of birth, intelligence value and speed value.

Character Class:
Attributes:
CharacterName : STRING, stores the name of the character
DateOfBirth : DATE, stores the date of birth of the character
Intelligence : REAL, stores the intelligence value of the character
Speed : INTEGER, stores the speed value of the character

Methods:
Constructor(), initialises CharacterName, DateOfBirth, Intelligence and Speed to the parameter values
SetIntelligence(), assigns the value of the parameter to Intelligence
GetIntelligence(), returns the value of Intelligence
GetName(), returns the name of the character
ReturnAge(), calculates and returns the age of the character as an integer
Learn(), increases the value of Intelligence by 10%

(a) (i) Write program code to declare the class Character and its constructor.
"""
import datetime as dt

class Character:
    # Attributes
    # PRIVATE CharacterName : STRING
    # PRIVATE DateOfBirth : DATE
    # PRIVATE Intelligence : REAL
    # PRIVATE Speed : INTEGER

    # Constructor
    def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed):
        self.__CharacterName = CharacterName
        self.__DateOfBirth = DateOfBirth
        self.__Intelligence = Intelligence
        self.__Speed = Speed

    """
    (ii) The get methods GetIntelligence() and GetName() return the attribute values.
    Write program code for the methods GetIntelligence() and GetName().
    """
    # Get methods / Accessor methods / Getters
    def GetIntelligence(self):
        return self.__Intelligence
    
    def GetName(self):
        return self.__CharacterName
    
    """
    (iii) The method SetIntelligence() assigns the value of its parameter to the attribute.
    Write program code for SetIntelligence().
    """
    # Set method / Mutator method / Setter
    def SetIntelligence(self, Intelligence):
        self.__Intelligence = Intelligence
    
    """
    The method Learn() increases the current value of Intelligence by 10%.
    Write program code for Learn().
    """
    def Learn(self):
        self.__Intelligence *= 1.1
    
    """
    (v) The method ReturnAge() calculates and returns the age of the character in years as
    an integer.
    Assume that the current year is 2023 and only use the year from the date of birth for the
    calculation. For example, the method returns 18 if the character was born on any date in
    2005.
    
    Write program code for the method ReturnAge().
    """

    def ReturnAge(self):
        current_year = 2023
        dob_year = self.__DateOfBirth.year # .year is a method of the datetime object
        age = current_year - dob_year
        return age
        # return 2023 - self.__DateOfBirth.year
 
"""
Program code for the class Character is given below.
(b) (i) Write program code to create a new instance of Character with the identifier
FirstCharacter.
The name of the character is Royal, date of birth is 1 January 2019, intelligence is 70
and speed is 30.

# Create a new instance of Character with the identifier FirstCharacter
FirstCharacter = Character("Royal", dt.datetime(2019, 1, 1), 70, 30)


(ii) Write program code to call the method Learn() for the character created in part 3(b)(i).
Output the name, age and intelligence of the character in an appropriate message.

# Call the method Learn() for the character created in part 3(b)(i)
FirstCharacter.Learn() # 70 * 1.1 = 77

# Output the name, age and intelligence of the character in an appropriate message
# Name: Royal, Age: 4, Intelligence: 77
print(f"Name: {FirstCharacter.GetName()}, Age: {FirstCharacter.ReturnAge()}, Intelligence: {FirstCharacter.GetIntelligence()}")
"""

# Writing child class code for MagicCharacter
"""
(c) The class MagicCharacter inherits from the class Character. A magic character has an
element, for example, water. This element changes how they learn. The magic character's
element is stored in the additional attribute Element.
MagicCharacter Class:
Element : STRING, stores the element for the character

Methods:
Constructor(), takes Element, CharacterName, DateOfBirth, Intelligence and Speed as parameters
calls its parent class constructor with the appropriate values initialises Element to its parameter value

Learn(), alters the intelligence of the character depending on the character's element

(i) Write program code to declare the class MagicCharacter and its constructor.
"""

class MagicCharacter(Character):
    # Attributes
    # PRIVATE Element : STRING

    # Constructor
    def __init__(self, Element, CharacterName, DateOfBirth, Intelligence, Speed):
        # Call the parent class constructor
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)

        self.__Element = Element

    """
    (ii) The method Learn() overrides the parent class method and increases the intelligence
    depending on the character's element.
        • If the element is fire or water, intelligence increases by 20%.
        • If the element is earth, intelligence increases by 30%.
        • If the element is not fire, water or earth the intelligence increases by 10%.
    Write program code for Learn().
    """

    def Learn(self): # overriding the parent class method, polymorphism
        if self.__Element == "fire" or self.__Element == "water":
            self.SetIntelligence(self.GetIntelligence() * 1.2)
        elif self.__Element == "earth":
            self.SetIntelligence(self.GetIntelligence() * 1.3)
        else:
            self.SetIntelligence(self.GetIntelligence() * 1.1)
    
"""
(d) (i) Write program code to create a new instance of MagicCharacter with the identifier
FirstMagic.
The name of the character is Light, date of birth is 3 March 2018, intelligence is 75,
speed is 22 and element is fire.
"""
# Create a new instance of MagicCharacter with the identifier FirstMagic
FirstMagic = MagicCharacter("fire", "Light", dt.datetime(2018, 3, 3), 75, 22)

"""
(ii) Write program code to call the method Learn() for the character created in part 3(d)(i).
Output the name, age and intelligence of the character in an appropriate message.
"""
# Call the method Learn() for the character created in part 3(d)(i)
FirstMagic.Learn() # 75 * 1.2 = 90

# Output the name, age and intelligence of the character in an appropriate message
# Name: Light, Age: 5, Intelligence: 90
print(f"Name: {FirstMagic.GetName()}, Age: {FirstMagic.ReturnAge()}, Intelligence: {FirstMagic.GetIntelligence()}")