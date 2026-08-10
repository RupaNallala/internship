def get_valid_age(): 
    try: 
        age = int(input("Enter your age: ")) 
        if age < 0:
             raise ValueError("Age cannot be negative.") 
             return age 
             except ValueError as error: 
                print("Invalid age:", error) 
                return None
                 student_age = get_valid_age() 
if student_age is not None: 
    print("Student age:", student_age())