courses=[]
max_total_units=18
while input("add a course (yes) ?") == "yes":
    courses.append({
        "course": input("enter the name : "),
        "professor":{
            "first name": input("enter first name : "),
            "last name":input("enter last name: ")
            },
        "units": int(input("enter the number of units : ")),
        "date":tuple(input("enter the date : "))
    })
    if sum["units"]==max_total_units:
        break
    elif sum["units"]>max_total_units:
        print("you are not able to have more than 17 units")

print("courses list: ")
print("Courses: " , " Professor:    ", "Units: ", " Date: ")
for i in courses:
    print(i["course"], i["professor"], i["units"],i["date"])