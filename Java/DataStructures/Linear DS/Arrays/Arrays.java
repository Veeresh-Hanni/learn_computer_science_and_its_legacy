
public class Arrays {
    public static void main(String[] args) {
        int[] numbers = { 1, 9, 2 }; // Declare , initialize
        System.out.println("Number of elements in the array = " + numbers.length);
        numbers[0] = 10;
        System.out.println("Values in the array numbers \n");
        printElements(numbers);

        int[] ages = new int[3];
        ages[0] = 50;
        ages[1] = 60;
        ages[2] = 70;
        System.out.println("\n Values in the ages  \n");
        printElements(ages);

        int[][] matrix = {
                { 1, 2, 3 },
                { 4, 5, 6 },
        };

        printElements2(ages);

        System.out.println("\n Values in the matrix  \n");
        // System.out.print(" " + matrix[0][0]);
        // System.out.print(matrix[0][1]);
        // System.out.print(matrix[0][2]);

        java.util.Arrays.sort(numbers);
        printElement_2d(matrix);

    }

    public static void printElements(int[] elements) {
        // Generating the sequential array index from 0 to length-1
        for (int index = 0; index < elements.length; index++) {
            System.out.print(" " + elements[index] + " ");
        }
    }

    public static void printElements2(int[] elements) {
        // Generating the sequential array index from 0 to length-1
        for (int element : elements) {
            System.out.print(" " + element + " ");
        }
    }

    public static void printElement_2d(int[][] elements) {

        for (int row = 0; row < elements.length; row++) { // rows
            for (int col = 0; col <= elements[row].length - 1; col++) { // columns in that row
                System.out.print(elements[row][col] + " ");
            }
            System.out.println(); // new line after each row
        }
    }

}