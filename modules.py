product=[]
total_count=0

def test(info,total_count):
    if info_dict["In"]==True:
        total_count += info_dict["Count"]
        product.append(info)
    elif info_dict["Out"]==True:
        if total_count<info_dict["Count"]:
            print("Not enough product")
        else:
            total_count -= info_dict["Count"]
            product.append(info)


def get_info (Product,Count,Price,Invar,Outvar):
    info={
        "Product":Product,
        "Count":Count,
        "Price":Price,
        "Person":Person,
        "In":Invar,
        "Out":Outvar
    }
    return info

def reset():
    Product.set("")
    Count.set(0)
    Price.set(0)
    Person.set("")
    Invar.set(False)
    Outvar.set(False)
