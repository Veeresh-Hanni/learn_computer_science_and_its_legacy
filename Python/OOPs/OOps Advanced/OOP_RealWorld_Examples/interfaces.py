
# interfaces.py
# Real-world Example: E-commerce Payment Gateways (Interface-like)

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Razorpay(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} INR using Razorpay.")

class Stripe(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} USD using Stripe.")

def process_payment(payment_method: PaymentGateway, amount: float):
    payment_method.pay(amount)

if __name__ == "__main__":
    razorpay = Razorpay()
    stripe = Stripe()
    process_payment(razorpay, 5000)
    process_payment(stripe, 100)
