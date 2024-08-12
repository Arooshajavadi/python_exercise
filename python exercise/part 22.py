from products_module import *
while input("add product (yes) ? ") == "yes":
    product= get_product()

    if sum_product(product_list) + product["price"] <= 1000:
        product_list.append(product)
        print("product added successfully !")
    else:
        print("products can not be more than 1000 $ !")

print("-----------------")
print_product(product_list)