#الگو ادرس
import re
address= input("enter your address :")
if re.match(r"^[a-z A-Z _\s ,]+$", address):
        print("welcome")
else:
        print("invalid")
    
