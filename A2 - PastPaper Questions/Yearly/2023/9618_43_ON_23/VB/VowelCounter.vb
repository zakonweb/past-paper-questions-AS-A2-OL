
Function IterativeVowels(Value As String) As Integer
    Dim Total As Integer
    Dim FirstCharacter As String
    Total = 0
    While Len(Value) > 0
        FirstCharacter = Left(Value, 1)
        If InStr("aeiou", FirstCharacter) > 0 Then
            Total = Total + 1
        End If
        Value = Mid(Value, 2)
    Wend
    IterativeVowels = Total
End Function

Function RecursiveVowels(Value As String) As Integer
    If Len(Value) = 0 Then
        RecursiveVowels = 0
    Else
        If InStr("aeiou", Left(Value, 1)) > 0 Then
            RecursiveVowels = 1 + RecursiveVowels(Mid(Value, 2))
        Else
            RecursiveVowels = RecursiveVowels(Mid(Value, 2))
        End If
    End If
End Function

' Example calls
Sub Main()
    console.writeline(IterativeVowels("house"))
    console.writeline(Debug.Print RecursiveVowels("imagine"))
End Sub
