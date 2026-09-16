# Q46: Custom InsufficientStockError
class InsufficientStockError(Exception):
    pass

stock = 10

try:
    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    if quantity > stock:
        raise InsufficientStockError("Not enough stock.")
    print("Order accepted.")
except InsufficientStockError as e:
    print("Error:", e)
except ValueError as e:
    print("Error:", e)
