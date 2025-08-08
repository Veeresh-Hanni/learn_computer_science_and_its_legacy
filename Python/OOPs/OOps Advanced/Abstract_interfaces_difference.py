from abc import ABC, abstractmethod

# Step 1: Define an interface-like abstract base class
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

# Step 2: Concrete class implementing ALL abstract methods
class PayPal(PaymentGateway):
    def pay(self, amount):
        print(f"PayPal Payment: {amount}")

    def refund(self, amount):
        print(f"PayPal Refund: {amount}")

# Step 3: Abstract class partially implementing methods
class BaseGateway(PaymentGateway):
    def pay(self, amount):
        print(f"Base Gateway Payment: {amount}")
    # refund() left unimplemented → subclasses must implement

# Step 4: Concrete subclass completing the abstract class
class Razorpay(BaseGateway):
    def refund(self, amount):
        print(f"Razorpay Refund: {amount}")

# MAIN EXECUTION
if __name__ == "__main__":
    # Working concrete implementation
    paypal = PayPal()
    paypal.pay(1000)
    paypal.refund(200)

    # Abstract + Concrete implementation
    razorpay = Razorpay()
    razorpay.pay(5000)
    razorpay.refund(300)

    # Uncomment to see error: Can't instantiate abstract class with unimplemented methods
    # gateway = BaseGateway()  # TypeError
