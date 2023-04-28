Module Module1

    Sub Main()
        Dim strLine As String
        Dim successful As Boolean
        Dim more, myChar As Char
        Do
            strLine = GetInfo()
            myChar = Left(strLine, 1)

            If myChar >= "A" And myChar <= "M" Then
                successful = WriteInfo(strLine, "File1.txt")
            Else
                successful = WriteInfo(strLine, "File2.txt")
            End If

            If successful = True Then
                Console.Write("Adding more records? (Y/N:)") : more = Console.ReadLine
            Else
                more = "N"
            End If
        Loop Until UCase(more) = "N"

    End Sub
    Function GetInfo() As String
        Dim uID, PreName, returnStr As String
        Dim isValid As Boolean = True
        Dim thisChar As Char
        Dim i As Integer

        Do
            Console.Write("Enter user ID (A9999): ") : uID = Console.ReadLine
            isValid = True

            thisChar = Left(uID, 1)
            If Len(uID) <> 5 Then
                isValid = False
            ElseIf thisChar < "A" Or thisChar > "Z" Then
                isValid = False
            Else
                For i = 2 To 5
                    thisChar = Mid(uID, i, 1)
                    If thisChar < "0" Or thisChar > "9" Then
                        isValid = False
                        Exit For
                    End If
                Next
            End If
        Loop Until isValid = True
        Console.Write("Enter preffered name: ") : PreName = Console.ReadLine

        returnStr = uID & "*" & PreName
        Return returnStr
    End Function


    Function WriteInfo(ByVal lineString As String, ByVal FName As String) As Boolean
        FileOpen(1, FName, OpenMode.Append)
        WriteLine(1, lineString)
        FileClose(1)
        Return True
    End Function

End Module
