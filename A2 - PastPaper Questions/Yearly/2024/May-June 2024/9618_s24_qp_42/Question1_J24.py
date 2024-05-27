'''1 A program outputs a main word. The program asks the user to enter the different words of 3 or
more letters that can be made from the letters in the main word. These are called the answers.
There are 3 files: Easy.txt, Medium.txt and Hard.txt. Each file has the main word on the
first line. For example, the main word in Easy.txt is house.
The answers are stored in the file. Each answer is on a new line after the main word. For example,
Easy.txt has 14 answers that can be made from the letters in house.
The words read from the text file are stored in the global array WordArray. The number of words
that can be made from the letters in the main word is stored in the global variable NumberWords.
(a) The procedure ReadWords():
• takes a file name as a parameter
• opens the file and reads in the data
• stores the main word in the first element in WordArray
• stores each answer in a new element in WordArray
• counts and stores the number of answers.
Write program code for the procedure ReadWords().'''
# Global variables
WordArray = []
NumberWords = 0

def ReadWords(filename):
    global WordArray, NumberWords
    with open(filename, 'r') as file:
        WordArray = file.read().splitlines()
    NumberWords = len(WordArray) - 1  # Exclude the main word

    '''(d) (i) The procedure ReadWords()calls Play()after the data in the file has been read.
    Write program code to amend ReadWords().'''
    Play()

'''(c) (i) The procedure Play():
• outputs the main word from the array and the number of answers
• allows the user to enter words until they enter the word 'no' to indicate they want to stop
• outputs whether each word the user enters is an answer or not an answer
• counts the number of answers the user gets correct
• replaces each answer that the user gets correct with a null value in the array.
Write program code for the procedure Play().'''

def Play():
    global WordArray, NumberWords
    main_word = WordArray[0]
    print(f"Main word: {main_word}")
    print(f"Number of answers: {NumberWords}")
    
    correct_answers = 0
    
    while True:
        user_word = input("Enter a word (or 'no' to stop): ").strip().lower()
        if user_word == 'no':
            break
        elif user_word in WordArray[1:]:
            print(f"{user_word} is an answer.")
            correct_answers += 1
            WordArray[WordArray.index(user_word)] = None  # Remove the word
        else:
            print(f"{user_word} is not an answer.")
    
    '''(ii) Amend the procedure Play()so that when the user enters the command to stop, the procedure:
    • outputs the percentage of answers the user entered from the array
    • outputs all the answers that the user did not enter.
    Write program code to amend Play().'''
    percentage_correct = (correct_answers / NumberWords) * 100
    print(f"Percentage of correct answers: {round(percentage_correct,2)}%")  # Round to 2 decimal places
    print("Answers you missed: ", [word for word in WordArray[1:] if word is not None])

'''(b) The main program asks the user to enter "easy", "medium" or "hard" and calls
ReadWords()with the filename that matches the user's input. For example, if the user enters
"easy", the parameter is "Easy.txt".

Write program code for the main program.'''
# main program
difficulty = input("Enter difficulty (easy, medium, hard): ").strip().lower()
if difficulty == "easy":
    ReadWords("Easy.txt")
elif difficulty == "medium":
    ReadWords("Medium.txt")
elif difficulty == "hard":
    ReadWords("Hard.txt")
else:
    print("Invalid input.")
# End of program
# Zafar Ali Khan (the ZAK)
# GitHub: zakonweb