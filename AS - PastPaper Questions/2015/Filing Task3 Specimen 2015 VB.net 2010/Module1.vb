Module Module1
    'TASK 3
    'Create a folder "C:\temp" first manually to ad a file to
    Dim path As String = "c:\temp\MyTest2.txt"

    Sub Main()
        'TASK 3.1
        'Create a text file if it already does not exist, and delete and recreate if it exisits
        If Not System.IO.File.Exists(path) Then
            'Craete and open file
            Using sw As System.IO.StreamWriter = System.IO.File.CreateText(path)
                sw.WriteLine("serial")
                sw.WriteLine("file organisation with data items in no particular order")
                sw.WriteLine("sequential")
                sw.WriteLine("file organisation where the data items are in some key field order")
                sw.WriteLine("file")
                sw.WriteLine("collection of data items")
                sw.WriteLine("input")
                sw.WriteLine("file mode which allows data to be written to the file")
                sw.WriteLine("output")
                sw.WriteLine("file mode which allows data to be read from the file")
                sw.WriteLine("append")
                sw.WriteLine("file mode which allows new data items to be added to the end of the file")
                sw.WriteLine("FILEREAD")
                sw.WriteLine("pseudocode term to read a data item from a file")
                sw.WriteLine("FILEWRITE")
                sw.WriteLine("pseudocode term to write a data item to a file")
                sw.WriteLine("EOF")
                sw.WriteLine("pseudocode for a function which returns TRUE/FALSE to indicate whether the end of file has been reached.")
            End Using 'close file
        End If

        'TASK 3.2
        'main menu
        Dim MenuPick As Integer
        Do
            Console.WriteLine()
            Console.WriteLine("1. Search for a term")
            Console.WriteLine("2. Search for key word in the descriptions")
            Console.WriteLine("3. End")
            Console.Write("Key in choice    ")
            MenuPick = Console.ReadLine()
            Select Case MenuPick
                Case 1 : Call SearchByTerm()
                Case 2 : SearchDescriptionsForKeyword()
                Case 3 'This case to avoid Case Else when pressed 0 to Exit
                Case Else
                    Console.WriteLine("Wrong Choice. Try gain or enter 3 to exit.")
                    Console.ReadKey()
            End Select
        Loop Until MenuPick = 3

    End Sub

    'Task 3.3
    Sub SearchByTerm()
        Dim Term, line As String

        Console.Write("Term.. ? ")
        Term = Console.ReadLine()

        ' Open the file to read from.  
        Using sr As System.IO.StreamReader = System.IO.File.OpenText(path)
            line = sr.ReadLine()
            Do While Not line Is Nothing  'While Line <> ""
                If line = Term Then
                    line = sr.ReadLine()
                    Console.WriteLine("FOUND ..." & line)
                    Console.ReadKey()
                    Exit Sub
                End If
                line = sr.ReadLine()
            Loop    'END WHILE
        End Using
        Console.WriteLine("TERM NOT FOUND")
        Console.ReadKey()

    End Sub

    'TASK 3.4
    Sub SearchDescriptionsForKeyword()
        Dim Term, line, keyword As String
        Dim IsFound As Boolean = False

        Console.Write("Key word.. ? ")
        keyword = Console.ReadLine()

        ' Open the file to read from.  
        Using sr As System.IO.StreamReader = System.IO.File.OpenText(path)

            'read term and description from the file
            Term = sr.ReadLine()
            line = sr.ReadLine()

            Do While Not line Is Nothing
                If InStr(line, keyword) > 0 Then
                    IsFound = True

                    Console.WriteLine("FOUND for " & Term)
                    Console.WriteLine(line)
                    Console.WriteLine()
                End If
                Term = sr.ReadLine()
                line = sr.ReadLine()
            Loop

        End Using

        If IsFound = False Then
            Console.WriteLine("NO DESCRIPTIONS FOUND containing this keyword.")
        End If

        Console.ReadKey()
    End Sub
End Module
