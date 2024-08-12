course_list=[]
while input("add course (y) : ") == "y":
    course={
        "lesson": input("enter lesson : "),
        "teacher": input("enter teacher : "),
        "unit": int(input("enter unit : "))
    }
    course_list.append(course)
upper_list= list(filter(lambda course: course["unit"]>5,course_list))
less_list= list(filter(lambda course: course["unit"]<5,course_list))
teacher_list=list(filter(lambda teacher: course["teacher"] == "alipour",upper_list))
teacher_list=list(filter(lambda teacher: course["teacher"] == "alipour",less_list))
print(upper_list)
print(less_list)
print("-----------")
print(teacher_list)