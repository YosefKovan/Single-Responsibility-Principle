from classes.payment.Payment import Payment

class PayPalPayment(Payment):

    def pay(self, amount):
        print(f"Pay pal payment {amount}")