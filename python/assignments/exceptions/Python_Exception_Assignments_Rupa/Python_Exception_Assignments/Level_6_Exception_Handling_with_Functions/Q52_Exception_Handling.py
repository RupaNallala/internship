# Q52: Function to calculate factorial
def factorial(number):
    if number < 0 or int(number) != number:
        raise ValueError("Enter a non-negative whole number.")
    result = 1
    for i in range(1, int(number) + 1):
        result *= i
    return result

try:
    number = float(input("Enter a number: "))
    print("Factorial:", factorial(number))
except ValueError as e:
    print("Error:", e)
