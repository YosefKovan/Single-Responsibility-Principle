from classes.payment.Payment import Payment

class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Credit card payment : {amount}" )

