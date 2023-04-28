
Module Module1

    'Task 1.2

    Sub Main()
        Dim FName, SName As String
        Console.Write("Enter First Name: ")
        FName = Console.ReadLine
        Console.Write("Enter Second Name: ")
        SName = Console.ReadLine
        Console.WriteLine(UCase(Left(FName, 1)) & LCase(Right(FName, Len(FName) - 1)) & " " & UCase(Left(SName, 1)) & LCase(Right(SName, Len(SName) - 1)))
        Console.WriteLine(UCase(Left(FName, 1)) & " " & UCase(Left(SName, 1)) & LCase(Right(SName, Len(SName) - 1)))
        Console.WriteLine(UCase(Left(SName, 1)) & LCase(Right(SName, Len(SName) - 1)) & _
                                                        ", " & UCase(Left(FName, 1)) & LCase(Right(FName, Len(FName) - 1)))
        Console.WriteLine("Mr " & UCase(Left(FName, 1)) & " " & UCase(Left(SName, 1)) & LCase(Right(SName, Len(SName) - 1)))
        Console.WriteLine("Dear Mr " & UCase(Left(SName, 1)) & LCase(Right(SName, Len(SName) - 1)))
        Console.WriteLine("First name: " & UCase(Left(FName, 1)) & LCase(Right(FName, Len(FName) - 1)) & ", Second name: " & UCase(Left(SName, 1)) & LCase(Right(SName, Len(SName) - 1)))
        Console.WriteLine(UCase(Left(FName, 1)) & LCase(Right(FName, Len(FName) - 1)) & " " & UCase(SName))
        Call User()
        Call User2()
        Console.ReadKey()
    End Sub


    'Task 1.3

    Sub User()
        Dim UserId As String
        Console.Write("Enter User ID: ")
        UserId = Console.ReadLine
        If Len(UserId) <> 6 Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf Left(UserId, 1) < "A" Or Left(UserId, 1) > "Z" Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf Mid(UserId, 2, 1) < "a" Or Mid(UserId, 2, 1) > "z" Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf Mid(UserId, 3, 1) < "a" Or Mid(UserId, 3, 1) > "z" Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf Val(Mid(UserId, 4, 1)) < 0 Or Val(Mid(UserId, 4, 1)) > 9 Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf Val(Mid(UserId, 5, 1)) < 0 Or Val(Mid(UserId, 5, 1)) > 9 Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf Val(Mid(UserId, 6, 1)) < 0 Or Val(Mid(UserId, 6, 1)) > 9 Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        Else : Console.WriteLine("Correct Format")
        End If

    End Sub


    'Task 2.3

    Sub User2()

        Dim UserId As String
        Console.Write("Enter User ID: ")
        UserId = Console.ReadLine
        If Len(UserId) <> 6 Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf UCase(Left(UserId, 1)) < "A" Or UCase(Left(UserId, 1)) > "Z" Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf UCase(Mid(UserId, 2, 1)) < "A" Or UCase(Mid(UserId, 2, 1)) > "Z" Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf UCase(Mid(UserId, 3, 1)) < "A" Or UCase(Mid(UserId, 3, 1)) > "Z" Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf Val(Mid(UserId, 4, 1)) < 0 Or Val(Mid(UserId, 4, 1)) > 9 Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf Val(Mid(UserId, 5, 1)) < 0 Or Val(Mid(UserId, 5, 1)) > 9 Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        ElseIf Val(Mid(UserId, 6, 1)) < 0 Or Val(Mid(UserId, 6, 1)) > 9 Then
            Console.WriteLine("Wrong Format")
            Exit Sub
        Else : Console.WriteLine("Correct Format")
        End If


    End Sub

End Module
