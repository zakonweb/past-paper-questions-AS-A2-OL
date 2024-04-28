
import java.util.EmptyStackException;
import java.util.Stack;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Question3 {
    private static Stack<String> animalStack = new Stack<>();
    private static Stack<String> colourStack = new Stack<>();

    public static void main(String[] args) {
        readData();
        for (int i = 0; i < 4; i++) {
            outputItem();
        }
    }

    private static void readData() {
        try (BufferedReader animalReader = new BufferedReader(new FileReader("AnimalData.txt"))) {
            String animal;
            while ((animal = animalReader.readLine()) != null) {
                animalStack.push(animal.trim());
            }
        } catch (IOException e) {
            System.out.println("Error reading file or file not found: AnimalData.txt");
        }

        try (BufferedReader colourReader = new BufferedReader(new FileReader("ColourData.txt"))) {
            String colour;
            while ((colour = colourReader.readLine()) != null) {
                colourStack.push(colour.trim());
            }
        } catch (IOException e) {
            System.out.println("Error reading file or file not found: ColourData.txt");
        }
    }

    private static void outputItem() {
        String animal = "";
        String colour = "";
        try {
            animal = animalStack.pop();
        } catch (EmptyStackException e) {
            System.out.println("No more animals.");
        }

        try {
            colour = colourStack.pop();
        } catch (EmptyStackException e) {
            System.out.println("No more colours.");
        }

        if (!animal.isEmpty() && !colour.isEmpty()) {
            System.out.println(colour + " " + animal);
        } else if (!animal.isEmpty()) {
            System.out.println("No colour " + animal);
        } else if (!colour.isEmpty()) {
            System.out.println(colour + " No animal");
        }
    }
}
