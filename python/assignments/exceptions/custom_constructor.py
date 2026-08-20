class InvalidAgeError(Exception): 
    def __init__(self, age, message="Age must be 18 or above."):
         self.age = age 
         self.message = message
          super().__init__(self.message)
          try: age = int(input("Enter age: ")) 
if age < 18:
     raise InvalidAgeError(age) 
except InvalidAgeError as error: 
    print("Registration failed:", error)
 else:
     print("Registration successful