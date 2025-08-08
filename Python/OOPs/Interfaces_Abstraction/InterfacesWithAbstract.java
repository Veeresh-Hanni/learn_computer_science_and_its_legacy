package Interfaces_Abstraction;

// Interface: A blueprint with method declarations only (no implementations)
// Any class implementing this interface MUST implement all its methods (unless the class is abstract)
interface PaymentGateway {
    void pay(double amount); // abstract method for payment

    void refund(double amount); // abstract method for refund
}

// Concrete class implementing the interface
// Must provide implementations for ALL interface methods
class PayPal implements PaymentGateway {

    // Implementing pay method from PaymentGateway interface
    @Override
    public void pay(double amount) {
        System.out.println("PayPal pay: " + amount);
    }

    // Implementing refund method from PaymentGateway interface
    @Override
    public void refund(double amount) {
        System.out.println("PayPal refund: " + amount);
    }
}

// Abstract class that partially implements the interface
// Provides a common implementation for 'pay' method but leaves 'refund'
// abstract
abstract class BaseGateway implements PaymentGateway {

    // Common implementation for pay method
    @Override
    public void pay(double amount) {
        System.out.println("Common pay logic");
    }

    // refund() method is NOT ❌ implemented here, so this class remains abstract
    // Any subclass must implement the refund method
}

// Concrete class extending the abstract BaseGateway class
// Since BaseGateway didn't implement refund(), this class must implement it
class Razorpay extends BaseGateway {

    // Implementing refund method that was missing in BaseGateway
    @Override
    public void refund(double amount) {
        System.out.println("Razorpay refund: " + amount);
    }
}

// Main class to test the implementations
public class InterfacesWithAbstract {
    public static void main(String[] args) {

        // ❌ Error: Cannot instantiate an interface
        // PaymentGateway pg_way = new PaymentGateway();

        // ✅ Creating object of PayPal class (fully implemented)
        PayPal paypal = new PayPal();
        paypal.pay(23.000); // Output: PayPal pay: 23.0
        paypal.refund(10.0); // Output: PayPal refund: 10.0

        // ❌ Error: Cannot instantiate an abstract class
        // BaseGateway base_gateway = new BaseGateway();

        // ✅ Creating object of Razorpay class (extends BaseGateway and implements
        // refund())
        Razorpay raz = new Razorpay();
        raz.pay(99.99); // Output: Common pay logic (from BaseGateway)
        raz.refund(123.45); // Output: Razorpay refund: 123.45
    }
}
