name_list=[]
while (name:=input("Enter name :  ")) != "exit":
    name_list.append(name)
    more_than_five=list(filter(lambda name: len(name)>5 , name_list))
    less_than_five=list(filter(lambda name: len(name)<5 , name_list))

print("more than five: ",more_than_five)
print("less than five: ",less_than_five)