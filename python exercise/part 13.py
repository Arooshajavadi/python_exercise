#دو عدد از کاربر دریافت کنید و از عدد کوچک تا عدد بزرگ را چاپ کنید(a,b)
a = int(input("enter your first number :"))

b = int(input("enter your second number :"))

for i in range(a,b+1,1):
    print(i)