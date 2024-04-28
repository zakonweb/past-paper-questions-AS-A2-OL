
' Declaration of DataArray to store 25 integers
Dim DataArray(24) As Integer

Sub Main()
    ' Initialize DataArray with zeros
    Dim i As Integer
    For i = 0 To 24
        DataArray(i) = 0
    Next i
    
    ' Reading data from file into DataArray
    On Error GoTo ErrorHandler
    Dim fileNumber As Integer
    fileNumber = FreeFile
    Open "Data.txt" For Input As #fileNumber
    For i = 0 To 24
        Input #fileNumber, DataArray(i)
    Next i
    Close #fileNumber
    Exit Sub
    
ErrorHandler:
    MsgBox "Error reading file or file not found.", vbCritical
End Sub

' Procedure to print array
Sub PrintArray(arr() As Integer)
    Dim j As Integer
    For j = LBound(arr) To UBound(arr)
        Print arr(j); " ";
    Next j
    Print
End Sub

' Function for linear search
Function LinearSearch(arr() As Integer, value As Integer) As Integer
    Dim count As Integer
    count = 0
    Dim k As Integer
    For k = LBound(arr) To UBound(arr)
        If arr(k) = value Then
            count = count + 1
        End If
    Next k
    LinearSearch = count
End Function
