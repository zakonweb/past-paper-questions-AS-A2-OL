class Horse:
    # Attributes (declared as private):
    # PRIVATE Name : STRING
    # PRIVATE MaxFenceHeight : INTEGER
    # PRIVATE PercentageSuccess : INTEGER

    def __init__(self, name, max_height, success_rate):
        self.__Name = name
        self.__MaxFenceHeight = max_height
        self.__PercentageSuccess = success_rate
    
    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

    def Success(self, height, risk):
        if height > self.__MaxFenceHeight:
            return self.__PercentageSuccess * 0.2
        else:
            if risk == 5:
                modifier = 0.6
            elif risk == 4:
                modifier = 0.7
            elif risk == 3:
                modifier = 0.8
            elif risk == 2:
                modifier = 0.9
            elif risk == 1:
                modifier = 1.0
            else:
                modifier = 0  # fail-safe (shouldn't occur if risk is validated)

            return self.__PercentageSuccess * modifier


# Fence class definition
class Fence:
    # Attributes (declared as private):
    # PRIVATE Height : INTEGER
    # PRIVATE Risk : INTEGER

    def __init__(self, height, risk):
        self.__Height = height
        self.__Risk = risk

    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk

# Main Program
# Declare list to hold 2 Horse objects
Horses = [None for i in range(2)] # Or: [None] * 2

# Instantiate and store Horse objects
Horses[0] = Horse("Beauty", 150, 72)
Horses[1] = Horse("Jet", 160, 65)

# Output names using GetName()
print(Horses[0].GetName())
print(Horses[1].GetName())

# Create Course array to store 4 Fence objects
Course = [None for _ in range(4)]

for i in range(4):
    valid = False   # falg
    while not valid:
        height_input = input(f"Enter height for fence {i+1} (in cm): ")
        risk_input = input(f"Enter risk for fence {i+1} (1 to 5): ")
        
        if height_input.isdigit() and risk_input.isdigit(): # type check
            height = int(height_input)
            risk = int(risk_input)
            if (70 <= height <= 180) and (1 <= risk <= 5): # range check
                Course[i] = Fence(height, risk)
                valid = True
            else:
                print("Invalid input. Height must be > 0 and risk must be between 1 and 5.")
        else:
            print("Invalid input. Please enter numbers only.")

''' # ei
for horse in Horses:
    for i in range(4):  # 4 fences
        height = Course[i].GetHeight()
        risk = Course[i].GetRisk()
        chance = round(horse.Success(height, risk), 2)
        print(f"The horse {horse.GetName()} at fence {i + 1} has a {chance}% chance of success")
'''

# eii - Store names and averages
highest_average = 0
top_horse_name = ""

for horse in Horses:
    total_chance = 0

    for i in range(4):  # 4 fences
        height = Course[i].GetHeight()
        risk = Course[i].GetRisk()
        chance = horse.Success(height, risk)
        total_chance += chance

    average = total_chance / 4
    average_rounded = round(average, 2)

    print(f"The horse {horse.GetName()} has an average {average_rounded}% chance of jumping over all four fences")

    if average > highest_average:
        highest_average = average
        top_horse_name = horse.GetName()

print(f"The horse with the highest average chance of success is {top_horse_name}")