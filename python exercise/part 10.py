#لیست اعداد بخش پذیر به سه و پنج در بازه ۱۰۰۰ تا ۲۰۰۰
numbers=[]
for i in range(1002,1999,3):
    numbers.append(i)
for i in range(1000,2001,5):
    numbers.append(i)
average=sum(numbers)//len(numbers)
print(average) 
