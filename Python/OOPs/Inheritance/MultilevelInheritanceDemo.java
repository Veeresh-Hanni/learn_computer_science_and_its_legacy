package Inheritance;

// Base Class
class User {
    String name = "Default User";
    String email = "default@example.com";

    void login() {
        System.out.println(name + " logged in using email: " + email);
    }
}

// Intermediate Class (inherits from User)
class Customer extends User {
    int cartItems = 0;

    void addToCart() {
        cartItems++;
        System.out.println(name + " added item to cart. Total items: " + cartItems);
    }
}

// Derived Class (inherits from Customer → multilevel inheritance)
class PrimeCustomer extends Customer {
    void getFreeDelivery() {
        System.out.println(name + " gets free delivery as Prime Customer.");
    }
}

// Main class to run the program
public class MultilevelInheritanceDemo {
    public static void main(String[] args) {
        PrimeCustomer prime = new PrimeCustomer();
        prime.name = "Veeresh";
        prime.email = "veeresh@example.com";

        prime.login(); // From User class
        prime.addToCart(); // From Customer class
        prime.getFreeDelivery(); // From PrimeCustomer class
    }
}
