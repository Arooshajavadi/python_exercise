person_list=[]
male_list=[]
female_list=[]

while input("add person (yes) ? ") == "yes":
    person={
        "name": input("Enter name : "),
        "gender": input("enter gender (f/m) : ")
    }
    person_list.append(person)

    for person in person_list:
        male_list=list(filter(lambda person: person["gender"] == "male" , person_list ))
        female_list=list(filter(lambda person: person["gender"] == "female" , person_list))

print("male: ",male_list)
print("female: ",female_list)