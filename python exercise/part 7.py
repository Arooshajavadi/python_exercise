#الگو شماره تماس
import re
phone_number= input("enter your phone number : ")
if re.match(r"09[0-9]{9}", phone_number ) or re.match(r"+98[0-9]{10}", phone_number ):
    print("ok")
else:
    print("invalid")

