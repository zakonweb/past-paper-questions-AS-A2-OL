
import java.io.*;
import java.util.Scanner;

public class Question1 {

    private static int[] dataArray = new int[25];

    public static void main(String[] args) {
        readData();
        printArray(dataArray);
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a whole number between 0 and 100 inclusive: ");
        int value = scanner.nextInt();
        while (value < 0 || value > 100) {
            System.out.println("Invalid input. Please enter a whole number between 0 and 100 inclusive.");
            value = scanner.nextInt();
        }
        int count = linearSearch(dataArray, value);
        System.out.println("The number " + value + " is found " + count + " times.");
    }

    private static void readData() {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("Data.txt"));
            for (int i = 0; i < dataArray.length; i++) {
                dataArray[i] = Integer.parseInt(reader.readLine().trim());
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("Error reading file or file not found.");
        }
    }

    private static void printArray(int[] array) {
        for (int j : array) {
            System.out.print(j + " ");
        }
        System.out.println();
    }

    private static int linearSearch(int[] array, int value) {
        int count = 0;
        for (int j : array) {
            if (j == value) {
                count++;
            }
        }
        return count;
    }
}
