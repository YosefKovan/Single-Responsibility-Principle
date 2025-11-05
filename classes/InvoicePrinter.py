

class InvoicePrinter:

    @staticmethod
    def print_invoice(order):

        print("Items: ")
        for item in order.items:
            print(item)

        print(f"Total price : {order.total_price}")