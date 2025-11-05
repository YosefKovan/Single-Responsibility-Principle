from classes.payment.Payment import Payment

class CryptoPayment(Payment):

      def pay(self, amount):
          print(f"Crypto payment : {amount}")


