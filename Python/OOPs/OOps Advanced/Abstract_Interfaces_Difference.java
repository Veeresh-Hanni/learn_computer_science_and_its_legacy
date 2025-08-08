
/*
 * Project: Payment Gateway Example
 * Demonstrates Interface, Abstract Class, and Concrete Class implementation in Java.
 */

// Step 1: Define an interface with method declarations only.
interface PaymentGateway {
    void pay(double amount); // Must be implemented by any concrete class

    void refund(double amount); // Must be implemented by any concrete class
}

// Step 2: A concrete class that implements ALL interface methods (works fine).
class PayPal implements PaymentGateway {
    @Override
    public void pay(double amount) {
        System.out.println("PayPal Payment: " + amount);
    }

    @Override
    public void refund(double amount) {
        System.out.println("PayPal Refund: " + amount);

        // Rule in Java
        // If a class implements an interface and is NOT abstract
        // → It must implement ALL interface methods.

        // If a class is declared abstract and implements an interface
        // → It can implement some (or one) of the methods.
        // → Subclasses (concrete classes) must implement the remaining methods.
    }
}

/*
 * // Step 3: A concrete class that does NOT implement all interface methods
 * (Uncomment to see compiler error).
 * class Stripe implements PaymentGateway {
 * 
 * @Override
 * public void pay(double amount) {
 * System.out.println("Stripe Payment: " + amount);
 * }
 * // refund() is missing → Compile-time error
 * }
 */

// Step 4: An abstract class that implements one method but leaves another
// unimplemented.
abstract class BaseGateway implements PaymentGateway {
    @Override
    public void pay(double amount) {
        System.out.println("Base Gateway Payment: " + amount);
    }

    // refund() left unimplemented → subclasses must implement it
}

// Step 5: A concrete class that extends the abstract class and implements the
// remaining method.
class Razorpay extends BaseGateway {
    @Override
    public void refund(double amount) {
        System.out.println("Razorpay Refund: " + amount);
    }
}

// Step 6: Main class to test all implementations.
public class Abstract_Interfaces_Difference {
    public static void main(String[] args) {
        // Concrete implementation (Interface → Concrete Class)
        PaymentGateway paypal = new PayPal();
        paypal.pay(1000);
        paypal.refund(200);

        // Abstract + Concrete implementation (Interface → Abstract → Concrete)
        PaymentGateway razorpay = new Razorpay();
        razorpay.pay(5000);
        razorpay.refund(300);

        // Uncomment Stripe class to see compiler error for unimplemented method.
        // PaymentGateway stripe = new Stripe();
    }
}
