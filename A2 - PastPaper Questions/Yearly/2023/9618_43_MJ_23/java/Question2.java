
class Vehicle {
    private String ID;
    private int MaxSpeed;
    private int CurrentSpeed;
    private int IncreaseAmount;
    private int HorizontalPosition;

    public Vehicle(String ID, int MaxSpeed, int IncreaseAmount) {
        this.ID = ID;
        this.MaxSpeed = MaxSpeed;
        this.IncreaseAmount = IncreaseAmount;
        this.CurrentSpeed = 0;
        this.HorizontalPosition = 0;
    }

    public int getCurrentSpeed() {
        return CurrentSpeed;
    }

    public int getIncreaseAmount() {
        return IncreaseAmount;
    }

    public int getHorizontalPosition() {
        return HorizontalPosition;
    }

    public int getMaxSpeed() {
        return MaxSpeed;
    }

    public void setCurrentSpeed(int speed) {
        this.CurrentSpeed = speed;
    }

    public void setHorizontalPosition(int position) {
        this.HorizontalPosition = position;
    }

    public void increaseSpeed() {
        CurrentSpeed += IncreaseAmount;
        if (CurrentSpeed > MaxSpeed) {
            CurrentSpeed = MaxSpeed;
        }
        HorizontalPosition += CurrentSpeed;
    }
}

class Helicopter extends Vehicle {
    private int VerticalPosition;
    private int MaxHeight;
    private int VerticalChange;

    public Helicopter(String ID, int MaxSpeed, int IncreaseAmount, int VerticalChange, int MaxHeight) {
        super(ID, MaxSpeed, IncreaseAmount);
        this.VerticalChange = VerticalChange;
        this.MaxHeight = MaxHeight;
        this.VerticalPosition = 0;
    }

    public int getVerticalPosition() {
        return VerticalPosition;
    }

    public void increaseSpeed() {
        super.increaseSpeed();
        VerticalPosition += VerticalChange;
        if (VerticalPosition > MaxHeight) {
            VerticalPosition = MaxHeight;
        }
    }
}

public class Question2 {

    public static void main(String[] args) {
        Vehicle car = new Vehicle("Tiger", 100, 20);
        Helicopter helicopter = new Helicopter("Lion", 350, 40, 3, 100);

        car.increaseSpeed();
        car.increaseSpeed();
        outputVehicleInfo(car);

        helicopter.increaseSpeed();
        helicopter.increaseSpeed();
        outputVehicleInfo(helicopter);
    }

    public static void outputVehicleInfo(Vehicle vehicle) {
        System.out.println("Horizontal Position: " + vehicle.getHorizontalPosition());
        System.out.println("Current Speed: " + vehicle.getCurrentSpeed());
        if (vehicle instanceof Helicopter) {
            System.out.println("Vertical Position: " + ((Helicopter) vehicle).getVerticalPosition());
        }
    }
}
