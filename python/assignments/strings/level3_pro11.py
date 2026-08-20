password=input("enter password")
for ch in password:
 if ch.isdigit():
    print("it conatins digit")
    break
 else :
    print("it doesnot contains the digit")