
# polymorphism.py
# Real-world Example: Payment Processing (Polymorphism)

class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of {amount}")

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

# Duck typing - any class with process_payment works
class CryptoPayment:
    def process_payment(self, amount):
        print(f"Processing cryptocurrency payment of {amount}")

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

if __name__ == "__main__":
    cc = CreditCardPayment()
    pp = PayPalPayment()
    crypto = CryptoPayment()
    for method in [cc, pp, crypto]:
        make_payment(method, 1000)
