#لیست اعداد سه رقمی زوج
numbers=[]
for i in range(100,1000,1):
    if i % 2==0:
        numbers.append(i)

print(sum(numbers))
