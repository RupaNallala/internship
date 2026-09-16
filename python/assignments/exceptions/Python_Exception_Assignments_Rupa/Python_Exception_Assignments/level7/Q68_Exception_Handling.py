# Q68: ShoppingCart with invalid products and quantities
class InvalidProductError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.products = {"Pen": 10, "Notebook": 5, "Bag": 2}

    def add(self, product, quantity):
        if product not in self.products:
            raise InvalidProductError("Product not found.")
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be positive.")
        if quantity > self.products[product]:
            raise InvalidQuantityError("Requested quantity is not available.")
        return "Product added to cart."

cart = ShoppingCart()

try:
    product = input("Enter product: ")
    quantity = int(input("Enter quantity: "))
    print(cart.add(product, quantity))
except (InvalidProductError, InvalidQuantityError) as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid quantity.")
