try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise Exception("Marks should be between 0 and 100.")

    print("Valid Marks")

except Exception as e:
    print(e)