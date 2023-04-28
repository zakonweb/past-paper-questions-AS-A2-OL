# Raul writes a program which will keep a tally of the number of times each letter appears in a
# given text. He uses an array of size 26 to store the totals for each letter. He then initialised
# each element of the array.
#   (a)	What value should Raul give each element?						[1]
#   (b) 	Define the array and initialise each element of the array using a high-level programming language of your choice.
#		Language
#		Code				    							[4]
#	(c)	Write the statements required to update the array when a letter has been read.	[3]

mySTR = "Writethestatementsrequiredtoupdatethearraywhenaletterhasbeenread".upper()

# Initialise
ltrArr = [0 for i in range(26)]

# Update
for count in mySTR:
    index = ord(count) - 65
    ltrArr[index] = ltrArr[index] + 1

for count in range(26):
    print(ltrArr[count])