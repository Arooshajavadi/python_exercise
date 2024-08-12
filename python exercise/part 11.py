#لیست اعداد بخش پذیر به پنج در بازه ۱۰۰۰ تا ۲۰۰۰
numbers=[]
for i in range(1000,2001,5):
    numbers.append(i) 

average=sum(numbers)//len(numbers)
print(average)

