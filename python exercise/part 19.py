#از کاربر تعداد ماشین های نمایشگاه را دریافت کن و نام،مدل و قیمت انها را دریافت کن و قیمت کل را اعلام کن
car_list =[]
total_price=0
number= int(input("enter the number of cars : ")) 
for car in range (1,number+1,1):
    car_list.append({
        "Name": input("enter the name : "),
        "Model": int(input("enter the model : ")),
        "Price": int(input("enter the price : "))
})

print("--------------------------------")
print("Report :")
print("Name :","Model :")
for cars in car_list:
    total_price += cars["Price"]
    print(cars["Name"] , cars["Model"] , "===>" , "Price : ", cars["Price"])

print("--------------------------------")
print("Total Price ====> ", total_price ,"$")