# Interfaces1.py
from abc import ABC, abstractmethod

# Interfaces 
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount): pass
    @abstractmethod
    def refund(self, amount): pass

# Concrete class must implement both
class PayPal(PaymentGateway):
    def pay(self, amount): print("PayPal pay:", amount)
    def refund(self, amount): print("PayPal refund:", amount)

# Abstract class can leave one unimplemented
class BaseGateway(PaymentGateway):
    def pay(self, amount): print(f"Base pay: {amount}")
    # refund() left unimplemented # Cause ann Error in Python must implement
    def refund(self, amount): print("Base Pay refund:", amount)
