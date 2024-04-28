'''
A  computer  program  is  being  developed  that  uses  a  set  of  cards. The  program  is  written  using  
object-oriented programming.
 The program has two classes: Card and Hand.
 The methods and attributes of these classes are shown:

Card class:
# Attributes
Number : INTEGER    # stores the card number from 1 to 5 inclusive
Colour : STRING     # stores the card colour: red, blue or yellow

# Methods
Constructor()   # takes a number and colour as parameters and sets the private values to these parameters

GetNumber()     # returns the card number
GetColour()     # returns the card colour

Hand class:
# Attributes
# Containment relationship, it is when one class contains an object of another class as an attribute
Cards : ARRAY[0:9] OF Card  # 1D array of type Card, stores up to 10 cards

FirstCard : INTEGER     # stores the position of the first card in the hand
NumberCards : INTEGER   # stores the number of cards in the hand

# Methods
Constructor()   # takes five card objects as parameters, assigns each 
                card to the array Cards[], initialises FirstCard to 0 
                and NumberCards to 5

GetCard()       # takes an index as a parameter and returns the card at 
                that index in the array Cards[]
'''

'''
(a) (i)  Write program code to declare the class Card, its attributes and constructor. 
Do not write program code for the get methods. 
Use your programming language appropriate constructor.
All attributes must be private. If you are writing in Python, include attribute declarations 
using comments
'''
class Cards:
    # Attributes
    # PRIVATE Number : INTEGER    # stores the card number from 1 to 5 inclusive
    # PRIVATE Colour : STRING     # stores the card colour: red, blue or yellow

    # Constructor
    def __init__(self, number, colour):
        self.__number = number
        self.__colour = colour
    
    # GetNumber()     # returns the card number
    # GetColour()     # returns the card colour
    def GetNumber(self):
        return self.__number
    
    def GetColour(self):
        return self.__colour

'''
(b) (i)  Write program code to declare the class Hand, its attributes and constructor.
Do not write the get methods. 
Use your programming language appropriate constructor.
All attributes must be private. If you are writing in Python, include attribute declarations 
using comments.
'''
class Hand:
    # Attributes
    # PRIVATE Cards : ARRAY[0:9] OF Card  # 1D array of type Card, stores up to 10 cards
    # PRIVATE FirstCard : INTEGER     # stores the position of the first card in the hand
    # PRIVATE NumberCards : INTEGER   # stores the number of cards in the hand

    # Constructor
    def __init__(self, card1, card2, card3, card4, card5):
        self.__cards = [card1, card2, card3, card4, card5] # initialise the array with 5 cards
        self.__firstCard = 0
        self.__numberCards = 5

    '''
    (ii) The get method GetCard() takes an index as a parameter and returns the card stored 
    at that index in the array.
    Write program code for the method GetCard().
    '''

    def GetCard(self, index):
        return self.__cards[index]

'''
(iii) The program is tested with the following cards:
    Number  Colour
    1       red
    2       red
    3       red
    4       red
    5       red
    1       blue
    2       blue
    3       blue
    4       blue
    5       blue
    1       yellow
    2       yellow
    3       yellow
    4       yellow
    5       yellow

Write  program  code  to  declare  each  of  these  cards  as  a  variable  of  type  Card  in  the main program
'''
# Create the cards
card1 = Cards(1, "red")
card2 = Cards(2, "red")
card3 = Cards(3, "red")
card4 = Cards(4, "red")
card5 = Cards(5, "red")
card6 = Cards(1, "blue")
card7 = Cards(2, "blue")
card8 = Cards(3, "blue")
card9 = Cards(4, "blue")
card10 = Cards(5, "blue")
card11 = Cards(1, "yellow")
card12 = Cards(2, "yellow")
card13 = Cards(3, "yellow")
card14 = Cards(4, "yellow")
card15 = Cards(5, "yellow")

'''
iii) Two players are declared with 5 cards each. 
   Player 1 has the cards: 1 red, 2 red, 3 red, 4 red, 1 yellow.
   Player 2 has the cards: 2 yellow, 3 yellow, 4 yellow, 5 yellow, 1 blue.
   Write program code to declare player 1 and player 2 as objects of type Hand, with the cards indicated.
'''
# Create the players
player1 = Hand(card1, card2, card3, card4, card11)
player2 = Hand(card12, card13, card14, card15, card6)

'''
c) The function CalculateValue() takes a player’s hand as a parameter and returns a score 
calculated using the following rules:
• If a card is red, 5 points are added to the player’s score.
• If a card is blue, 10 points are added to the player’s score.
• If a card is yellow, 15 points are added to the player’s score.
• The number of each card in the hand is added to the player’s score.
   (i) Write program code for the function CalculateValue().
   Assume that there are only 5 cards in the player’s hand in this function.
'''

def CalculateValue(player):
    score = 0
    for i in range(5):
        if player.GetCard(i).GetColour() == "red":
            score += 5
        elif player.GetCard(i).GetColour() == "blue":
            score += 10
        elif player.GetCard(i).GetColour() == "yellow":
            score += 15
        score += player.GetCard(i).GetNumber()
    return score

'''
ii) Amend the main program by writing program code to use the function  
CalculateValue() for each of the two players. The player with the highest score wins.
Output an appropriate message to identify the winning player, or if the game was a draw 
(both players have the same number of points).
'''
player1_score = CalculateValue(player1)
player2_score = CalculateValue(player2)

# print both players' scores
print("Player 1's score is", player1_score)
print("Player 2's score is", player2_score)

if player1_score > player2_score:
    print("Player 1 wins!")
elif player2_score > player1_score:
    print("Player 2 wins!")
else:
    print("It's a draw!")
# End of Question 2