
public class VowelCounter {
    // Iterative method to count vowels
    public static int IterativeVowels(String value) {
        int total = 0;
        int lengthString = value.length();
        for (int x = 0; x < lengthString; x++) {
            char firstCharacter = value.charAt(0);
            if ("aeiou".indexOf(firstCharacter) >= 0) {
                total += 1;
            }
            value = value.substring(1);
        }
        return total;
    }

    // Recursive method to count vowels
    public static int RecursiveVowels(String value) {
        if (value.isEmpty()) {
            return 0;
        } else {
            char firstCharacter = value.charAt(0);
            if ("aeiou".indexOf(firstCharacter) >= 0) {
                return 1 + RecursiveVowels(value.substring(1));
            } else {
                return RecursiveVowels(value.substring(1));
            }
        }
    }

    public static void main(String[] args) {
        System.out.println(IterativeVowels("house")); // Example call for IterativeVowels
        System.out.println(RecursiveVowels("imagine")); // Example call for RecursiveVowels
    }
}
