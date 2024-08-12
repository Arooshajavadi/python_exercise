#الگو ایمیل
import re
email= input("enter your email : ")

if re.match(r"^[a-z][\w.]{3,30}@(gmail|yahoo|msn)\.com$", email,re.I):
    print("ok")
else:
    print("invaid")
