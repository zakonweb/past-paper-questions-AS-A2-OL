
Class Vehicle
    ' Private attributes
    Private ID As String
    Private MaxSpeed As Integer
    Private CurrentSpeed As Integer
    Private IncreaseAmount As Integer
    Private HorizontalPosition As Integer
    
    ' Constructor
    Public Sub New(ByVal vehicleID As String, ByVal maxSpd As Integer, ByVal incrAmount As Integer)
        ID = vehicleID
        MaxSpeed = maxSpd
        IncreaseAmount = incrAmount
        CurrentSpeed = 0
        HorizontalPosition = 0
    End Sub
    
    ' Public methods for accessing and modifying private attributes
    Public Function GetCurrentSpeed() As Integer
        GetCurrentSpeed = CurrentSpeed
    End Function
    
    Public Function GetHorizontalPosition() As Integer
        GetHorizontalPosition = HorizontalPosition
    End Function
    
    Public Sub IncreaseSpeed()
        CurrentSpeed = CurrentSpeed + IncreaseAmount
        If CurrentSpeed > MaxSpeed Then CurrentSpeed = MaxSpeed
        HorizontalPosition = HorizontalPosition + CurrentSpeed
    End Sub
End Class

Class Helicopter
    Inherits Vehicle
    ' Additional attributes for Helicopter
    Private VerticalPosition As Integer
    Private VerticalChange As Integer
    Private MaxHeight As Integer
    
    ' Constructor for Helicopter
    Public Sub New(ByVal vehicleID As String, ByVal maxSpd As Integer, ByVal incrAmount As Integer, ByVal vertChange As Integer, ByVal maxHeight As Integer)
        MyBase.New(vehicleID, maxSpd, incrAmount)
        VerticalChange = vertChange
        MaxHeight = maxHeight
        VerticalPosition = 0
    End Sub
    
    ' Override IncreaseSpeed for Helicopter
    Public Overrides Sub IncreaseSpeed()
        MyBase.IncreaseSpeed()
        VerticalPosition = VerticalPosition + VerticalChange
        If VerticalPosition > MaxHeight Then VerticalPosition = MaxHeight
    End Sub
    
    ' Getter for VerticalPosition
    Public Function GetVerticalPosition() As Integer
        GetVerticalPosition = VerticalPosition
    End Function
End Class

Sub Main()
    ' Instantiate a car and a helicopter
    Dim car As Vehicle
    Set car = New Vehicle("Tiger", 100, 20)
    Dim helicopter As Helicopter
    Set helicopter = New Helicopter("Lion", 350, 40, 3, 100)
    
    ' Increase speed twice for the car
    car.IncreaseSpeed
    car.IncreaseSpeed

    ' Output car information
    Call OutputVehicleInfo(car)

    ' Increase speed twice for the helicopter
    helicopter.IncreaseSpeed
    helicopter.IncreaseSpeed

    ' Output helicopter information
    Call OutputVehicleInfo(helicopter)
End Sub

Sub OutputVehicleInfo(vehicle As Vehicle)
    MsgBox "Horizontal Position: " & vehicle.GetHorizontalPosition() & " Current Speed: " & vehicle.GetCurrentSpeed()
    If TypeName(vehicle) = "Helicopter" Then
        MsgBox "Vertical Position: " & Helicopter(vehicle).GetVerticalPosition()
    End If
End Sub
