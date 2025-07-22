
public class Datatypes {
    public static void main(String[] args) {
        // Primitive data types with proper variable names
        byte age = 100;
        byte storage = 102;
        short salary = 20000;
        int population = 123456789;
        long distance = 123456789012345L;
        float piValue = 3.14f;
        double precisePi = 3.14159265359;
        char grade = 'A';
        boolean isActive = true;
        // Reference data types with proper variable names
        String greeting = "Hello, Java!";
        int[] numbers = { 1, 2, 3, 4, 5 };
        Datatypes datataypesInstance = new Datatypes();
        // Display values
        System.out.println("byte (age): " + age);
        System.out.println("short (salary): " + salary);
        System.out.println("int (population): " + population);
        System.out.println("long (distance): " + distance);
        System.out.println("float (piValue): " + piValue);
        System.out.println("double (precisePi): " + precisePi);
        System.out.println("char (grade): " + grade);
        System.out.println("boolean (isActive): " + isActive);
        System.out.println("String (greeting): " + greeting);
        System.out.print("int[] (numbers): ");

        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
        System.out.println("Datataypes (datataypesInstance): " + datataypesInstance);
    }
}