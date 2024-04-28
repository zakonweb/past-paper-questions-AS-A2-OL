"""
2 A computer game is being designed that will include different vehicles. A prototype for the game is
being developed using object‑oriented programming.
The class Vehicle stores data about the vehicles. Each vehicle has an identification name,
a maximum speed, a current speed and a horizontal position. The value IncreaseAmount is
added to the current speed each time the vehicle increases its speed.
Vehicle Class
Attributes:
ID : STRING         # stores the identification name for the vehicle
MaxSpeed : INTEGER  # stores the maximum speed
CurrentSpeed : INTEGER  # stores the current speed
IncreaseAmount : INTEGER    # stores the amount CurrentSpeed increases by
HorizontalPosition : INTEGER    # stores the horizontal position

# Methods
# Constructor
Constructor()   # initialises ID, MaxSpeed and IncreaseAmount to the parameter values 
                # initialises both CurrentSpeed and HorizontalPosition to 0

# Getters/Accessors
GetCurrentSpeed() # returns the current speed
GetIncreaseAmount() # returns the increase amount
GetHorizontalPosition() # returns the horizontal position
GetMaxSpeed() # returns the maximum speed

# Setters/Mutators
SetCurrentSpeed() # assigns the parameter to the current speed
SetHorizontalPosition() # assigns the parameter to the horizontal position
IncreaseSpeed() # calculates and stores the new speed and horizontal position of the vehicle
"""

"""
(a) (i) Write program code to declare the class Vehicle. All attributes must be private.
You only need to declare the class and its constructor. Do not declare any other methods.
Use your programming language’s appropriate constructor.
If you are writing program code in Python, include attribute declarations using comments.
"""
# Class declaration
class Vehicle:
    # Attributes
    # PRIVATE ID : STRING
    # PRIVATE MaxSpeed : INTEGER
    # PRIVATE CurrentSpeed : INTEGER
    # PRIVATE IncreaseAmount : INTEGER
    # PRIVATE HorizontalPosition : INTEGER

    # Constructor
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = IncreaseAmount
        self.__HorizontalPosition = 0
    
    """
    (ii) Write program code for the get methods GetCurrentSpeed(), GetIncreaseAmount(), GetMaxSpeed() and GetHorizontalPosition()
    """
    # Getters/Accessors
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    # (iii) Write program code for the set methods SetCurrentSpeed() and SetHorizontalPosition()
    # Setters/Mutators
    def SetCurrentSpeed(self, speed):
        self.__CurrentSpeed = speed
    
    def SetHorizontalPosition(self, position):
        self.__HorizontalPosition = position

    """
    (iv) The method IncreaseSpeed():
        • adds IncreaseAmount to the current speed
        • adds the updated current speed to the horizontal position.
    The current speed of a vehicle cannot exceed its maximum speed.
    Write program code for the method IncreaseSpeed()
    """
    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount

        # Ensure the current speed does not exceed the maximum speed
        if self.__CurrentSpeed > self.__MaxSpeed: 
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed

"""
(b) The child class Helicopter inherits from the parent class Vehicle. A helicopter also has a
vertical position and changes the vertical position when it increases speed.

Helicopter Class, Inheriting from Vehicle
Attributes:
VerticalPosition : INTEGER  # stores the vertical position
VerticalChange : INTEGER    # stores the amount VerticalPosition changes by
MaxHeight : INTEGER # stores the maximum height the helicopter can reach

Constructor()   # takes the ID, maximum speed, increase amount, 
                # vertical change and maximum height as parameters
                # initialises the vertical position to 0

GetVerticalPosition()   # returns the vertical position
IncreaseSpeed() # calculates and stores the new speed, horizontal and vertical position of the helicopter

IncreaseSpeed is overridden in the Helicopter class to include the vertical position.
This is an example of polymorphism.
"""

"""
(i) Write program code to declare the class Helicopter. You only need to declare the
class and its constructor. You do not need to declare the other methods.
Use your programming language’s appropriate constructor.
All attributes must be private.
If you are writing in Python, include attribute declarations using comments.
"""
# Child Class declaration
class Helicopter(Vehicle):
    # Attributes
    # PRIVATE VerticalPosition : INTEGER
    # PRIVATE VerticalChange : INTEGER
    # PRIVATE MaxHeight : INTEGER

    # Constructor
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalChange
        self.__MaxHeight = MaxHeight

    # (ii) Write program code for the get method GetVerticalPosition()
    # Getters/Accessors
    def GetVerticalPosition(self):
        return self.__VerticalPosition

    """
    (ii) The Helicopter method IncreaseSpeed() overrides the method from the parent class and:
        • adds the amount of vertical change to the vertical position
        • adds IncreaseAmount to the current speed
        • adds the updated current speed to the horizontal position.
    The vertical position of a helicopter cannot exceed its maximum height.
    The current speed of a helicopter cannot exceed its maximum speed.
    Write program code for the method IncreaseSpeed()
    """
    def IncreaseSpeed(self): # Overriding the method, Polymorphism
        self.__VerticalPosition += self.__VerticalChange
        # Ensure the vertical position does not exceed the maximum height
        if self.__VerticalPosition > self.__MaxHeight: 
            self.__VerticalPosition = self.__MaxHeight

        self._Vehicle__CurrentSpeed += self._Vehicle__IncreaseAmount
        # Ensure the current speed does not exceed the maximum speed
        if self._Vehicle__CurrentSpeed > self._Vehicle__MaxSpeed: 
            self._Vehicle__CurrentSpeed = self._Vehicle__MaxSpeed
        self._Vehicle__HorizontalPosition += self._Vehicle__CurrentSpeed

"""
(c) A procedure needs to output the horizontal position and speed of a vehicle. If the vehicle is a helicopter, it also outputs the vertical position.
All outputs must include appropriate messages.
Write program code for this procedure.
"""
# Procedure to output vehicle information
def OutputVehicleInfo(vehicle):
    print("Horizontal Position:", vehicle.GetHorizontalPosition())
    print("Current Speed:", vehicle.GetCurrentSpeed())
    if isinstance(vehicle, Helicopter): # Check if the vehicle is a helicopter
        print("Vertical Position:", vehicle.GetVerticalPosition())

"""
(d) The main program needs to:
• instantiate a car as a new vehicle with the ID "Tiger", a maximum speed of 100 and an
increase amount of 20
• instantiate a new helicopter with the ID "Lion", a maximum speed of 350, an increase
amount of 40, a vertical change of 3 and a maximum height of 100
• call IncreaseSpeed() twice for the car and then call the output procedure from
part 2(c) for the car
• call IncreaseSpeed() twice for the helicopter and then call the output procedure from
part 2(c) for the helicopter.
(i) Write program code for the main program.
"""
# Main program
# Instantiate a car and a helicopter
car = Vehicle("Tiger", 100, 20)
helicopter = Helicopter("Lion", 350, 40, 3, 100)

# Increase speed twice for the car
car.IncreaseSpeed()
car.IncreaseSpeed()
# Output car information
OutputVehicleInfo(car)
print()

# Increase speed twice for the helicopter
helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
# Output helicopter information
OutputVehicleInfo(helicopter)