Module Module1
    'Raul writes a program which will keep a tally of the number of times each letter appears in a
    '	given text. He uses an array of size 26 to store the totals for each letter. He then initialised
    '	each element of the array.
    '	(a)	What value should Raul give each element?						[1]
    '	(b) 	Define the array and initialise each element of the array using a high-level
    '		programming language of your choice.
    '		Language
    '		Code				    							[4]
    '	(c)	Write the statements required to update the array when a letter has been read.	[3]

    Sub Main()
        Dim mySTR As String = UCase("Writethestatementsrequiredtoupdatethearraywhenaletterhasbeenread")
        Dim ch As String
        Dim ltrArr(26), count, index As Integer

        'Initialise
        For count = 1 To 26
            ltrArr(count) = 0
        Next

        'Update
        For count = 1 To Len(mySTR)
            ch = Mid(mySTR, count, 1)
            index = Asc(ch) - 64
            ltrArr(index) = ltrArr(index) + 1
        Next

        For count = 1 To 26
            Console.WriteLine(ltrArr(count))
        Next
        Console.ReadKey()
    End Sub

End Module
