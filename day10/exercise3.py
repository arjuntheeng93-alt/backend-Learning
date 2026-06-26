class CurrencyConverter:
    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        if from_currency == "USD" and to_currency == "Krw":
            return amount * 1350
        return amount
    
class PaypalGateway:
    def process_transaction(self, account_id, final_amount , currency):
        return f"Processing PayPal payment of {final_amount} {currency} for account{account_id} "
    
class StripeGateway:
    def process_transaction(self, card_number, final_amount, currency):
        return f"Processing Strip credit card payment of {final_amount} {currency} for card {card_number}"
    
class ApplePayGateway:
    def process_transaction(self, device_id, final_amount, currency):
        return f"Processing ApplePay payment of {final_amount} {currency} for devie{device_id}"
    
#after this we will implement composition\
    
class PaymentProcessor:
    def __init__(self, gateway, converter=None):
        self.gateway = gateway
        self.converter = converter or CurrencyConverter()
        
    def checkout(self, user_identifier, base_amount, base_currency, target_currency):
        final_amount = self.converter.convert(base_amount, base_currency, target_currency)
        
        return self.gateway.process_transaction(user_identifier, final_amount, target_currency)
    
Paypal_processor = PaymentProcessor(gateway = PaypalGateway())
print(Paypal_processor.checkout("user_ac@email.com", 100, "USD", "Krw"))

Stripe_processor = PaymentProcessor(gateway=StripeGateway())
print(Stripe_processor.checkout("234-345-245", 44,  "USD" , "USD"))

apple_processor = PaymentProcessor(gateway=ApplePayGateway())
print(apple_processor.checkout("AR-234", 30, "USD", "Krw"))
