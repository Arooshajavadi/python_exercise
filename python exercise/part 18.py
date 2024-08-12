product_list=[]
all_total=0
while input("add product (yes) ?") == "yes":
    product_list.append({
        "name": input("enter the name : "),
        "quantity": int(input("enter the quantity : ")),
        "price": int(input("enter the price : "))
      })
print("----------------------------------")
print("Report : ")
for i in product_list:
    item_total=i["quantity"] * i["price"]
    print(i["name"],i["quantity"],i["price"], "===>", item_total , "$")
    all_total += item_total
print("total price : ===>", all_total , "$")


#در قسمت گزارش و جمع مشکل داشتم