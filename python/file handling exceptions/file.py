# Program 1
# Aim: Create a text file and write your name, course, and city.

with open("student.txt", "w") as file:
    file.write("Name : Rupa\n")
    file.write("Course : Diploma CSE\n")
    file.write("City : Rajahmundry\n")

print("File created and data written successfully.")