#نحوه ساخت الگو کد ملی
import re
national_id=input( "enter your national id : ")
if re.match(r"[0-9]{10}", national_id) or re.match(r"[0-9]{3}-[0-9]{6}-[0-9]{1}", national_id):
    print("welcome")
else:
    print("invalid")
