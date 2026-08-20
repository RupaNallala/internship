# Q16: Database connection and finally
# This example uses SQLite, which is included with Python.
import sqlite3

connection = None

try:
    connection = sqlite3.connect("students.db")
    print("Database connected successfully.")
except sqlite3.Error as e:
    print("Database error:", e)
finally:
    if connection:
        connection.close()
        print("Database connection closed.")
