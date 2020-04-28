Module Module1

    Sub Main()
        Dim CS As Integer
        Dim Physics As Integer
        Dim Chemistry As Integer
        Dim Maths As Integer
        Dim Choice As Integer

        CS = 0
        Physics = 0
        Chemistry = 0
        Maths = 0
        Do
            Console.Write("Please enter choice (CS 1, Physics 2, Chemistry 3, Maths 4 or 0 to stop) : ")
            Choice = Console.ReadLine()
            Select Case Choice
                Case 1 : CS = CS + 1
                Case 2 : Physics = Physics + 1
                Case 3 : Chemistry = Chemistry + 1
                Case 4 : Maths = Maths + 1
            End Select
        Loop Until (Choice = 0)
        Console.WriteLine("Computer Science " & CS)
        Console.WriteLine("Physics " & Physics)
        Console.WriteLine("Chemistry " & Chemistry)
        Console.WriteLine("Maths " & Maths)

        Console.ReadKey()
    End Sub

End Module
