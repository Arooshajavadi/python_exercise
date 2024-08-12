#الگو نام
import re
name = input("Enter Name : ")
if re.match(r"[a-z A-Z/s]{3,30}", name):
    print("Ok", name)
else:
    print("Invalid")


