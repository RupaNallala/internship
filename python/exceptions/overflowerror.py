import math
 try:
     result = math.exp(1000)
 except OverflowError: 
    print("The result is too large.")  