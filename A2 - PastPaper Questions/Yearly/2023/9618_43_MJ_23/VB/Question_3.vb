
' Global arrays and variables
Dim Animal(19) As String
Dim Colour(9) As String
Dim AnimalTopPointer As Integer
Dim ColourTopPointer As Integer

Public Sub Main()
    ' Initialize pointers
    AnimalTopPointer = 0
    ColourTopPointer = 0

    ' Call ReadData procedure
    Call ReadData()

    ' Output items four times
    Call OutputItem()
    Call OutputItem()
    Call OutputItem()
    Call OutputItem()
End Sub

Public Sub ReadData()
    Dim i As Integer
    Dim animal As String
    Dim colour As String
    Dim result As Boolean
    On Error GoTo ErrorHandler
    
    ' Read animal data
    Open "AnimalData.txt" For Input As #1
    For i = 1 To 20
        If EOF(1) Then Exit For
        Line Input #1, animal
        result = PushAnimal(animal)
    Next i
    Close #1
    
    ' Read colour data
    Open "ColourData.txt" For Input As #2
    For i = 1 To 10
        If EOF(2) Then Exit For
        Line Input #2, colour
        result = PushColour(colour)
    Next i
    Close #2
    Exit Sub
    
ErrorHandler:
    MsgBox "Error reading file or file not found."
End Sub

Function PushAnimal(ByVal DataToPush As String) As Boolean
    If AnimalTopPointer >= 20 Then
        Return False
    Else
        Animal(AnimalTopPointer) = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        Return True
    End If
End Function

Function PushColour(ByVal DataToPush As String) As Boolean
    If ColourTopPointer >= 10 Then
        Return False
    Else
        Colour(ColourTopPointer) = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        Return True
    End If
End Function

Function PopAnimal() As String
    If AnimalTopPointer = 0 Then
        Return ""
    Else
        AnimalTopPointer = AnimalTopPointer - 1
        Return Animal(AnimalTopPointer)
    End If
End Function

Function PopColour() As String
    If ColourTopPointer = 0 Then
        Return ""
    Else
        ColourTopPointer = ColourTopPointer - 1
        Return Colour(ColourTopPointer)
    End If
End Function

Sub OutputItem()
    Dim animal As String
    Dim colour As String
    Dim result As Boolean
    animal = PopAnimal()
    colour = PopColour()
    If colour = "" Then
        If animal <> "" Then
            result = PushAnimal(animal)
            MsgBox "No colour"
        End If
    ElseIf animal = "" Then
        result = PushColour(colour)
        MsgBox "No animal"
    Else
        MsgBox colour & " " & animal
    End If
End Sub
