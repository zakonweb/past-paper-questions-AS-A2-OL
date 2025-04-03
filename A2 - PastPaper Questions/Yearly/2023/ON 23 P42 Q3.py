# 9618/42/O/N/23 Q3
'''
CharacterName : STRING
DateOfBirth : DATE
Intelligence : REAL
Speed : INTEGER
stores the name of the character
stores the date of birth of the character
stores the intelligence value of the character
stores the speed value of the character
Constructor()
initialises CharacterName, DateOfBirth,
Intelligence and Speed to the parameter values

SetIntelligence()
assigns the value of the parameter to Intelligence

GetIntelligence()
returns the value of Intelligence

GetName()
returns the name of the character

ReturnAge()
calculates and returns the age of the character as an integer

Learn()
increases the value of Intelligence by 10%
'''

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
    
    # Setters
    def SetIntelligence(self, Intelligence):
        self.__Intelligence = Intelligence
    
    # Getters
    def GetIntelligence(self):
        return self.__Intelligence
    
    def GetName(self):
        return self.__CharacterName
    
    def ReturnAge(self):
        # consider date is string and format is DD/MM/YYYY
        d,m,y = self.__DateOfBirth.split('/')
        return 2023 - int(y)
    
    # other methods
    def Learn(self):
        self.__Intelligence *= 1.1

'''
The class MagicCharacter inherits from the class Character. A magic character has an
element, for example, water. This element changes how they learn. The magic character’s
element is stored in the additional attribute Element.
MagicCharacter
Element : STRING stores the element for the character
Constructor()
Learn()
takes Element, CharacterName, DateOfBirth,
Intelligence and Speed as parameters
calls its parent class constructor with the appropriate values
initialises Element to its parameter value
alters the intelligence of the character depending on the
character’s element

The method Learn() overrides the parent class method and increases the intelligence
depending on the character’s element.
• If the element is fire or water, intelligence increases by 20%.
• If the element is earth, intelligence increases by 30%.
• If the element is not fire, water or earth the intelligence increases by 10%.
Write program code for Learn().
'''

class MagicCharacter(Character):
    # Attributes
    # PRIVATE Element : STRING

    # Constructor
    def __init__(self, Element, CharacterName, DateOfBirth, Intelligence, Speed):
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
        self.__Element = Element
    
    # other methods
    # Polymorphism
    def Learn(self):
        if self.__Element == 'fire' or self.__Element == 'water':
            self.SetIntelligence(self.GetIntelligence() * 1.2)
        elif self.__Element == 'earth':
            self.SetIntelligence(self.GetIntelligence() * 1.3)
        else:
            self.SetIntelligence(self.GetIntelligence() * 1.1)

'''
Write program code to create a new instance of Character with the identifier
FirstCharacter.
The name of the character is Royal, date of birth is 1 January 2019, intelligence is 70
and speed is 30.

FirstCharacter = Character('Royal', '01/01/2019', 70, 30)

FirstCharacter.Learn()

# Output the name, age and intelligence of the character in an appropriate message.
print(f'Name: {FirstCharacter.GetName()}')
print(f'Age: {FirstCharacter.ReturnAge()}')
print(f'Intelligence: {FirstCharacter.GetIntelligence()}')
'''

'''Write program code to create a new instance of MagicCharacter with the identifier
FirstMagic.
The name of the character is Light, date of birth is 3 March 2018, intelligence is 75,
speed is 22 and element is fire.
'''
FirstMagic = MagicCharacter('fire', 'Light', '03/03/2018', 75, 22)
FirstMagic.Learn()

#Output the name, age and intelligence of the character in an appropriate message.
print(f'Name: {FirstMagic.GetName()}')
print(f'Age: {FirstMagic.ReturnAge()}')
print(f'Intelligence: {FirstMagic.GetIntelligence()}')