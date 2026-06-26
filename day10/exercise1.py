#payment proccessor we wil learn abstractmethod here
from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    def __init__(self, currency="krw"):
        self.currency = currency
        
    @abstractmethod
    def charge(self, amount, customer_id):
        pass
    
    @abstractmethod
    def refund(self, transaction_id):
        pass
    
    def format_amount(self, amount):
        return f"{self.currency} {amount:.2f}"
    
    def __str__(self):
        return f"{self.__class__.__name__}(currency = {self.currency})"
    
class StripeProcessor(PaymentProcessor):
    def __init__(self):
        super().__init__ (currency = "krw")
        
    def charge(self, amount, customer_id):
        formatted = self.format_amount(amount)
        return f"Strip charged {formatted} to customer {customer_id}"
    def refund(self, transaction_id):
        return f"strip refunded transaction {transaction_id}"
    
class PaypalProcessor(PaymentProcessor):
    def __init__(self):
        super().__init__(currency = "krw")
        
    def charge(self, amount, customer_id):
        formatted = self.format_amount(amount)
        return f"Paypal Charged {formatted} to customer {customer_id}"
    
    def refund(self, transaction_id):
        return f" Paypal refunded transaction {transaction_id}"
    
    
class KakaoPayProcessor(PaymentProcessor):
    def __init__(self):
        super(). __init__ (currency = "krw")
        
    def charge(self, amount, customer_id):
        formatted = self.format_amount(amount)
        return f"kakaoPay charged {formatted} to customer {customer_id}"
    
    def refund(self, transaction_id):
        return f"kakoPay refunded transaction {transaction_id}"
    
processors = [
    StripeProcessor(),
    PaypalProcessor(),
    KakaoPayProcessor()
    
]

for processor in processors:
    print(processor)
    print(processor.charge(99.99, "user_123"))
    print(processor.refund("txtn_345"))
    print()
    
try:
    p = PaymentProcessor()
except TypeError as e:
    print(f"Error: {e}")