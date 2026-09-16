# Q59: Product price and invalid quantity
def calculate_price(price, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    return price * quantity

try:
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    print("Total price:", calculate_price(price, quantity))
except ValueError as e:
    print("Error:", e)
