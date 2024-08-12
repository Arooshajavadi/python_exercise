lesson_list=[]

def get_course():
    lesson ={
        "name": input("enter name : "),
        "teacher": input("enter teacher's name : "),
        "unit": int(input("enter unit : "))
    }
    return lesson


def total_units(lesson_list):
    total_vahed=0
    for lesson in lesson_list:
        total_vahed += lesson["unit"]
    return total_vahed 


def print_lessons(lesson_list):
    for lesson in lesson_list:
        print("   name : ", lesson["name"],"    teacher : ",lesson["teacher"],"    unit : ",lesson["unit"])