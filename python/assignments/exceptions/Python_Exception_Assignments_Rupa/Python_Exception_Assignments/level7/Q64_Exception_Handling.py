# Q64: Product class with insufficient stock exception
class InsufficientStockError(Exception):
    pass

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.stock:
            raise InsufficientStockError("Insufficient stock.")
        self.stock -= quantity
        return self.stock

product = Product("Notebook", 20)

try:
    quantity = int(input("Enter quantity to buy: "))
    print("Remaining stock:", product.sell(quantity))
except (InsufficientStockError, ValueError) as e:
    print("Error:", e)
