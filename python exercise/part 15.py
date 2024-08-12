#همانند تمرین چهارده اما روی اعداد منفی نیز جواب دهد
x= int(input("enter a number : "))
if x<0:
    for i in range(x,-x+1,1):
        print(i)
else:
    for i in range(-x,x+1,1):
        print(i)