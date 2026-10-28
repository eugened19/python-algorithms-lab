class PaymentGateway:
    def charge(self, amount):
        raise RuntimeError("Real payment attempted!")

class OrderService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def calculate_total(self, price, quantity):
        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity <= 0:
            raise ValueError("Invalid quantity")

        return price * quantity

    def checkout(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")

        return self.payment_gateway.charge(amount)



    