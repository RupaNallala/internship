# Q35: Product quantity validation
try:
    quantity = int(input("Enter product quantity: "))
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    print("Quantity accepted:", quantity)
except ValueError as e:
    print("Error:", e)
