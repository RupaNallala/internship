# Q67: Payment class with invalid payment exception
class InvalidPaymentAmountError(Exception):
    pass

class Payment:
    def pay(self, amount):
        if amount <= 0:
            raise InvalidPaymentAmountError("Payment amount must be positive.")
        return "Payment successful."

payment = Payment()

try:
    amount = float(input("Enter payment amount: "))
    print(payment.pay(amount))
except InvalidPaymentAmountError as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid amount.")
