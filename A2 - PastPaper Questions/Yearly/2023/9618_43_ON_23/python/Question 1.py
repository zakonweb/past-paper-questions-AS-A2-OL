"""
FUNCTION IterativeVowels(Value : STRING) RETURNS INTEGER
    DECLARE Total : INTEGER
    DECLARE LengthString : INTEGER
    DECLARE FirstCharacter : CHAR
    Total ← 0
    LengthString ← LENGTH(Value)
    FOR X ← 0 TO LengthString - 1
        FirstCharacter ← MID(Value, 0, 1)
        IF FirstCharacter = 'a' OR FirstCharacter = 'e' OR
            FirstCharacter = 'i' OR FirstCharacter = 'o' OR
            FirstCharacter = 'u' THEN
            Total ← Total + 1
        ENDIF
        Value ← MID(Value, 1, LENGTH(Value)-1)
    NEXT X
    RETURN Total
ENDFUNCTION
"""

# (a) (i) Write program code for the function IterativeVowels().
def IterativeVowels(Value):
    # DECLARE Total : INTEGER
    # DECLARE LengthString : INTEGER
    # DECLARE FirstCharacter : CHAR
    Total = 0
    LengthString = len(Value)
    for X in range(LengthString):
        FirstCharacter = Value[0]
        # if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
        if FirstCharacter in 'aeiou':
            Total += 1
        Value = Value[1:] # MID(Value, 1, LENGTH(Value)-1)
    return Total

'''
(b) (i) Rewrite the function IterativeVowels() as a recursive function with the identifier
RecursiveVowels().
'''

def RecursiveVowels(Value):
    if Value == "" or len(Value) == 0: # Base case
        return 0
    else: # Recursive case/Gneral case
        FirstCharacter = Value[0]
        if FirstCharacter in 'aeiou':
            return 1 + RecursiveVowels(Value[1:])
        else:
            return RecursiveVowels(Value[1:])

# (ii) Write program code to call the function IterativeVowels() with the parameter "house" from the main program.
# print(IterativeVowels("house"))

# (ii) Write program code to call the function RecursiveVowels() with the parameter "imagine" from the main program.
print(RecursiveVowels("imagine"))