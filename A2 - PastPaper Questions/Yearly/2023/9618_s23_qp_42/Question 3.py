"""
3 A company needs a computer program to store data about its employees.
Part of the program is being written using object-oriented programming.
The class Employee stores data about the employees. Each employee has an employee number, 
a job title and hourly pay rate. The class will also store the amount they are paid each week over a 
52-week year in a 1D array.
Employee Class

The class has the following attributes:
HourlyPay : REAL    # stores the amount each employee gets paid each hour
EmployeeNumber : STRING     # stores the employee's unique number
JobTitle : STRING   # stores the employee's job title
PayYear2022 : ARRAY[0:51] OF REAL # stores the amount the employee has been paid each week

# The class has the following methods:
Constructor()   # initialises HourlyPay, EmployeeNumber and JobTitle from the values passed as parameters, initialises all 52 elements in PayYear2022 to 0.0

GetEmployeeNumber() # returns the employee number
SetPay()    # takes the week number and number of hours worked that week as parameters
            # calculates and stores the pay for that week in PayYear2022

GetTotalPay()   # returns the total of all the values in PayYear2022
"""

"""
(a) (i)  Write program code to declare the class Employee. 
   You only need to declare the class and its constructor. Do not declare any other methods. 
   Use your programming language appropriate constructor. 
   If you are writing program code in Python, include attribute declarations using comments.
"""
class Employee:
    # Attributes
    # PRIVATE HourlyPay : REAL
    # PRIVATE EmployeeNumber : STRING
    # PRIVATE JobTitle : STRING
    # PRIVATE PayYear2022 : ARRAY[0:51] OF REAL

    # Constructor
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        # Attributes
        self.__HourlyPay = HourlyPay
        self.__EmployeeNumber = EmployeeNumber
        self.__JobTitle = JobTitle
        self.__PayYear2022 = [0.0 for i in range(52)]
    
    """
    (ii) The method GetEmployeeNumber() returns the employee number.
    Write program code for the method GetEmployeeNumber()
    """
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    """
    (iii) The method SetPay():
    • takes a week number and the number of hours worked that week as parameters
    • calculates  the  pay  for  that  week  by  multiplying  the  hourly  pay  by  the  number  of hours worked that week
    • stores the calculated pay in the appropriate index for that week in PayYear2022.
    Write program code for the method SetPay().
    """
    def SetPay(self, week_number, hours_worked):
        self.__PayYear2022[week_number] = self.__HourlyPay * hours_worked
    
    """
    (iv) The method GetTotalPay() returns the total of all the values in PayYear2022.
    Write program code for the method GetTotalPay().
    """
    def GetTotalPay(self):
        # return sum(self.__PayYear2022) # This will return the total pay for the year
        total = 0
        for i in self.__PayYear2022:
            total += i
        return total

"""
(b) The child class Manager inherits from the parent class Employee.
  A manager gets a bonus. This bonus value is a percentage, for example 10.0%. 
  When calculating the pay, the number of hours the manager worked that week is increased by the bonus value.

Manager Class
# The class has the following attributes:
BonusValue : REAL   #stores the bonus value, for example 10.0 represents a 10.0% increase

# The class has the following methods:
Constructor()  # initialises BonusValue from the value passed as a parameter
               # takes bonus value, hourly pay, employee number and job title as parameters

SetPay()    # takes the week number and number of hours worked that week as parameters
            # increases the number of hours worked by the bonus value
            # calls the SetPay() method from the parent class
"""

class Manager(Employee):
    # Attributes
    # PRIVATE BonusValue : REAL

    # Constructor
    def __init__(self, BonusValue, HourlyPay, EmployeeNumber, JobTitle):
        # Attributes
        self.__BonusValue = BonusValue
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
    """
    (ii) The Manager method SetPay() overrides the method from the parent class and:
    • takes the week number and number of hours worked as parameters
    • increases the number of hours worked by the bonus value
    • calls SetPay() from the parent class.
    Write program code for the method SetPay().
    """
    def SetPay(self, week_number, hours_worked):
        super().SetPay(week_number, hours_worked + (hours_worked * self.__BonusValue / 100))
    
"""
(c) The main program has a global 1D array, EmployeeArray, to store data about eight employees. Each employee is stored as an object of type Employee.
The file Employees.txt stores data about the employees, in the order:
• hourly pay
• employee number
• bonus value (where included)
• job title.
Only employees who are managers have a bonus value saved. For example:
• The first employee is a Junior Developer, with employee number 12452 and an hourly pay of $15.22. This employee does not have a bonus value.
• The third employee is an Interface Manager, with employee number 02586 and an hourly pay of $22.50. This employee has a bonus value of 5.25%.

Write the main program to:
• declare the array to store data about 8 employees
• read in the data from the file for each employee
• instantiate each employee as either Employee (if the employee does not have a bonus 
value) or Manager (if the employee has a bonus value).
"""
EmployeeArray = []
file = open("Employees.txt", "rt")
hourly_pay = file.readline().strip()
while hourly_pay:
    hourly_pay = float(hourly_pay)
    employee_number = file.readline().strip()
    temp = file.readline().strip()
    # check the first character of the line to see if it is a digit
    # if it is a digit, then it is a bonus value
    # if it is not a digit, then it is a job title
    #if temp[0].isdigit():
    if temp[0] in "0123456789":
        bonus_value = float(temp)
        job_title = file.readline().strip()
        EmployeeArray.append(Manager(bonus_value, hourly_pay, employee_number, job_title))
    else:
        job_title = temp
        EmployeeArray.append(Employee(hourly_pay, employee_number, job_title))
    hourly_pay = file.readline().strip()
file.close()

"""
d) The file HoursWeek1.txt stores the number of hours each employee has worked in week 1, in the order:
• employee number
• number of hours worked.
  For example, the first set of data is for employee 21548 who has worked 50.0 hours.
  The procedure EnterHours():
• reads in the values from the file
• finds the location of each employee in EmployeeArray
• calls the method SetPay() for each employee.
Write program code for EnterHours().
"""

def EnterHours():
    file = open("HoursWeek1.txt", "rt")
    employee_number = file.readline().strip()
    while employee_number:
        hours_worked = float(file.readline())
        for i in EmployeeArray:
            if i.GetEmployeeNumber() == employee_number:
                i.SetPay(1, hours_worked)
                break # break out of the loop once the employee is found
        employee_number = file.readline().strip()
    file.close()

"""
(e) (i) The main program needs to call EnterHours() and use the method GetTotalPay() to output the employee number and total pay for each of the eight employees.
Amend the main program to perform these tasks.
"""

EnterHours()

# All of the below methods are correct and can be used to print the output
"""
# Method 1
for i in range(len(EmployeeArray)):
    print(f"Employee Number: {EmployeeArray[i].GetEmployeeNumber()}\nTotal Pay: {EmployeeArray[i].GetTotalPay()}")
    print()
"""

"""
# Method 2
for i in EmployeeArray:
    print(f"Employee Number: {i.GetEmployeeNumber()}\nTotal Pay: {i.GetTotalPay()}")
    print()
"""

"""
# Method 3
To match the Marking Scheme we may need to read the data from the file HoursWeek1.txt and output the employee number and total pay for each employee in the order they are stored in the file.
"""
file = open("HoursWeek1.txt", "rt")
employee_number = file.readline().strip()
while employee_number:
    hours_worked = float(file.readline())
    for i in EmployeeArray:
        if i.GetEmployeeNumber() == employee_number:
            print(f"Employee Number: {i.GetEmployeeNumber()}\nTotal Pay: {i.GetTotalPay()}")
            print()
            break
    employee_number = file.readline().strip()
file.close()

# In any of the above method, marking scheme in not matching the output.
# In last case, most the output is matching the marking scheme but complete.
# This is probably because of the way the data is stored in the file
# End of Question 3