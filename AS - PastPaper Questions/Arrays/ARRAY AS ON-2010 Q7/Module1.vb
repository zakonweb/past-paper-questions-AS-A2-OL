Module Module1

    Sub Main()
        Dim YearTemp(11), total, M, Avg, Dif As Single
        Dim i, yt As Integer

        For i = 1 To 11
            YearTemp(i) = 0
        Next

        For i = 1 To 11
            yt = Console.ReadLine
            YearTemp(i) = yt
            total = total + yt
        Next
        M = total / 11
        total = 0

        Do
            yt = Console.ReadLine
        Loop Until yt >= 1 And yt <= 11


        For i = yt To (yt + 3)
            total = total + YearTemp(i)
        Next
        Avg = total / 4

        Dif = Avg - M

        If Dif > 4 Then
            Console.WriteLine("HOT")
        Else
            Console.WriteLine("COLD")
        End If
        Console.ReadKey()
    End Sub

End Module
