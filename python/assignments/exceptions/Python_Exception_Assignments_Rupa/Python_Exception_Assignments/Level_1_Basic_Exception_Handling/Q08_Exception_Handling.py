# Q8: Handle ModuleNotFoundError
try:
    import my_special_module
    print("Module imported successfully.")
except ModuleNotFoundError:
    print("The module was not found.")
