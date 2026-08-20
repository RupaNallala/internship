try: 
    number1 = int(input("Enter first number: ")) 
try: 
    number2 = int(input("Enter second number: "))
     print(number1 / number2) 
     except ZeroDivisionError: 
        print("Second number cannot be zero.")
except ValueError: 
    print("Enter integers only")