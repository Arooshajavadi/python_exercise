#درس هایی که تعداد واحد ان بیشتر از ۱۷ در مجموع نشود
from exercise_module import *
while input("add course (yes) ? ") == "yes":
    lesson = get_course()

    if total_units(lesson_list) + lesson["unit"] <=17:
        lesson_list.append(lesson)
        print("ok")
    else:
        print("units are full")

print("---------------")
print_lessons(lesson_list)