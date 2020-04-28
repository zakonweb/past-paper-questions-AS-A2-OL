Module Module1

    Sub Main()
        Dim NoArr(10) As Integer
        Dim c, i, j, x As Integer
        Dim alreadyFound As Boolean = False

        Randomize()
        c = 0
        For i = 1 To 10
            NoArr(i) = 0
        Next

        For i = 1 To 10
            Do
                c = c + 1
                alreadyFound = False
                x = Int(Rnd() * 20) + 1
                For j = i To 1 Step -1
                    If NoArr(j) = x Then alreadyFound = True
                Next
            Loop Until alreadyFound = False

            NoArr(i) = x
        Next

        For i = 1 To 10
            Console.WriteLine(NoArr(i))
        Next
        Console.WriteLine("Loop worked for " & c & " times.")
        Console.ReadKey()
    End Sub

End Module
