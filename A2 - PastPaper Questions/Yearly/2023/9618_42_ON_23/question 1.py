"""
1 A program stores lower-case letters in two stacks.
One stack stores vowels (a, e, i, o, u) and one stack stores consonants (letters that are not
vowels).
Each stack is implemented as a 1D array.
(a) (i) Write program code to declare two 1D global arrays: StackVowel and StackConsonant.
Each array needs to store up to 100 letters. The index of the first element in each array is 0.
If you are writing in Python, include declarations using comments.
"""
# global arrays
# stack to store vowels
StackVowel = ['' for i in range(100)]

# stack to store consonants
StackConsonant = ['' for i in range(100)]

"""
(ii) The global variable VowelTop is a pointer that stores the index of the next free space in
StackVowel.
The global variable ConsonantTop is a pointer that stores the index of the next free
space in StackConsonant.
VowelTop and ConsonantTop are both initialised to 0.
Write program code to declare and initialise the two variables.
If you are writing in Python, include declarations using comments.
"""
# DECLARE AND INITIALISE VARIABLES
# DECLARE VowelTop : INTEGER
# DECLARE ConsonantTop : INTEGER
VowelTop = 0
ConsonantTop = 0

"""
(b) (i) The procedure PushData() takes one letter as a parameter.
If the parameter is a vowel, it is pushed onto StackVowel and the relevant pointer
updated.
If the stack is full, a suitable message is output.
If the parameter is a consonant, it is pushed onto StackConsonant and the relevant
pointer updated.
If the stack is full, a suitable message is output.
You do not need to validate that the parameter is a letter.
Write program code for PushData().
"""

def PushData(letter):
    global VowelTop, ConsonantTop
    if letter in 'aeiou': # it is a vowel
        if VowelTop < 100:
            StackVowel[VowelTop] = letter
            VowelTop += 1
        else:
            print('StackVowel is full')
    else: # it is a consonant
        if ConsonantTop < 100:
            StackConsonant[ConsonantTop] = letter
            ConsonantTop += 1
        else:
            print('StackConsonant is full')

"""
(ii) The file StackData.txt stores 100 lower-case letters.
The procedure ReadData() reads each letter from the file and uses PushData() to
push each letter onto its appropriate stack.
Use appropriate exception handling if the file does not exist.
Write program code for ReadData().
"""

def ReadData():
    try:
        file = open('StackData.txt', 'rt')
        for letter in file: # each line has one letter
            PushData(letter.strip())
        file.close()
    except:
        print('File not found')
        return
    
"""
(c) The function PopVowel() removes and returns the data at the top of StackVowel and
updates the relevant pointer(s).
The function PopConsonant() removes and returns the data from the top of StackConsonant
and updates the relevant pointer(s).
If either stack is empty, the string "No data" must be returned.
Write program code to declare PopVowel() and PopConsonant().
"""

def PopVowel():
    global VowelTop
    if VowelTop > 0:
        VowelTop -= 1
        letter = StackVowel[VowelTop]
        return letter
    else:
        return 'No data'

def PopConsonant():
    global ConsonantTop
    if ConsonantTop > 0:
        ConsonantTop -= 1
        letter = StackConsonant[ConsonantTop]
        return letter
    else:
        return 'No data'

"""
(d) The program first needs to call ReadData() and then:
1. prompt the user to input their choice of vowel or consonant
2. take, as input, the user's choice
3. depending on the user's choice, call PopVowel() or PopConsonant() and store the
return value.
The three steps are repeated until 5 letters have been successfully returned and stored.
If either stack is empty at any stage, an appropriate message must be output.
Once 5 letters have been successfully returned and stored, they are output on one line, for
example:
abyti
(i) Write program code for the main program.
"""
# main program
choice = ''
count = 0
result = ''
ReadData()
while count < 5:
    # prompt the user to input their choice of vowel or consonant
    # through a menu
    print('vowel, or')
    print('consonant')
    choice = input('Enter your choice: ')

    if choice == 'vowel':
        letter = PopVowel()
        if letter == 'No data':
            print('StackVowel is empty')
        else:
            result += letter
    elif choice == 'consonant':
        letter = PopConsonant()
        if letter == 'No data':
            print('StackConsonant is empty')
        else:
            result += letter
    count += 1
print(result)