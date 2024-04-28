"""
2 An integer is said to be divisible by another integer if the result of the division is also an integer.
For example:
10 is divisible by 1, 2, 5 and 10:
• 10 ÷ 1 = 10
• 10 ÷ 2 = 5
• 10 ÷ 5 = 2
• 10 ÷ 10 = 1
10 is not divisible by 4:
• 10 ÷ 4 = 2.5
1, 2, 5 and 10 are said to be the divisors of 10.
The iterative function IterativeCalculate() totals all the divisors of its integer parameter and
returns this total.
Example 1: if the parameter is 10, the total will be 18 (1 + 2 + 5 + 10) .
Example 2: if the parameter is 4, the total will be 7 (1 + 2 + 4) .
A pseudocode algorithm for IterativeCalculate() is shown.
FUNCTION IterativeCalculate(Number : INTEGER) RETURNS INTEGER
    DECLARE Total : Integer
    DECLARE ToFind : Integer
    ToFind ← Number
    Total ← 0
    WHILE Number <> 0
        IF ToFind MODULUS Number = 0 THEN
            Total ← Total + Number
        ENDIF
        Number ← Number - 1
    ENDWHILE
    RETURN Total
ENDFUNCTION
The operator MODULUS calculates the remainder when one number is divided by another.
(a) (i) Write program code for IterativeCalculate().
"""

def IterativeCalculate(Number):
    Total = 0
    ToFind = Number
    while Number != 0:
        if ToFind % Number == 0: # % is the modulus operator
            Total += Number
        Number -= 1
    return Total

# Test the function
# print(IterativeCalculate(10)) # result is 18

"""
(b) IterativeCalculate() has been rewritten as the recursive function RecursiveValue().
A pseudocode algorithm for RecursiveValue() is given. The function is incomplete.
FUNCTION RecursiveValue(Number : INTEGER, ToFind : INTEGER) RETURNS INTEGER
    IF Number = .............. THEN
        RETURN 0
    ELSE
        IF ToFind .............. Number = 0 THEN
            RETURN .............. + RecursiveValue(Number - 1, ToFind)
        ELSE
            .............. RecursiveValue(Number - 1, ..............)
        ENDIF
    ENDIF
ENDFUNCTION

Complete the function RecursiveValue() by filling in the blanks.
FUNCTION RecursiveValue(Number : INTEGER, ToFind : INTEGER) RETURNS INTEGER
    IF Number = 0 THEN
        RETURN 0
    ELSE
        IF ToFind MOD Number = 0 THEN
            RETURN Number + RecursiveValue(Number - 1, ToFind)
        ELSE
            RETURN RecursiveValue(Number - 1, ToFind)
        ENDIF
    ENDIF
ENDFUNCTION
"""

# (i) Write program code for RecursiveValue().
def RecursiveValue(Number, ToFind):
    if Number == 0:
        return 0
    else:
        if ToFind % Number == 0:
            return Number + RecursiveValue(Number - 1, ToFind)
        else:
            return RecursiveValue(Number - 1, ToFind)

"""
(ii) Write program code to call RecursiveValue() with 50 as the first parameter and 50
as the second parameter and output the return value.
"""
# Test the function
print(RecursiveValue(10, 10)) # result is 18
print(RecursiveValue(50, 50)) # result is 93
