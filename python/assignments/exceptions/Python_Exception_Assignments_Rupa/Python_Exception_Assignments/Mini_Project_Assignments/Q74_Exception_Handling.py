# Q74: Shopping Cart System
class ProductError(Exception):
    pass

products = {"Pen": 10, "Notebook": 5, "Bag": 2}

try:
    product = input("Enter product: ")
    if product not in products:
        raise ProductError("Invalid product.")

    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        raise ProductError("Invalid quantity.")
    if quantity > products[product]:
        raise ProductError("Insufficient stock.")

    print("Added", quantity, product, "to cart.")
except ProductError as e:
    print("Error:", e)
except ValueError:
    print("Quantity must be an integer.")
