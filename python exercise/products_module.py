product_list =[]
def get_product():
    product ={    
        "name": input("enter the product's name : "),
        "number": int(input("enter number : ")),
        "price": int(input("enter price : "))
        }
    return product

def sum_product(product_list):
    total_price=0
    for product in product_list:
        total_price += product["price"]
    return total_price 


def print_product(product_list):
    for product in product_list:
        print("name : ", product["name"], ", number : ",product["number"],", price : ",product["price"])