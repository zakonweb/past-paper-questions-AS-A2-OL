Module Module1

    Sub Main()
        Call TestRandom(200)
    End Sub

    Sub TestRandom(ByVal Repetitions As Integer)
        Dim x As New Random
        Dim a, b, frequency(10), ExpFreq As Integer

        ExpFreq = Repetitions / 10
        Console.WriteLine("Ecpected Frequency is " & ExpFreq)

        For a = 1 To 10
            frequency(a) = 0
        Next

        For a = 1 To Repetitions
            b = x.Next(1, 11)
            frequency(b) = frequency(b) + 1
        Next

        Console.WriteLine("Number     Frequency    Difference")
        For a = 1 To 10
            Console.WriteLine(a & "     " & frequency(a) & "      " & ExpFreq - frequency(a))
        Next

        Console.ReadKey()
    End Sub
End Module
