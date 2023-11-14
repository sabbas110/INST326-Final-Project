from tkinter import *
from misc import Course

plan_complete = False
graduation_plan = {}
current_semester = -1

root = Tk()

myLabel = Label(root, text = "Welcome to the UMD College of Information Studies Degree Audit").grid(row = 0, column = 0)
myLabel2 = Label(root, text = "Majors:").grid(row = 1, column = 0)
myLabel3 = Label(root, text = "Information Science | Social Data Science | Technology and Information Design").grid(row = 2, column = 0)
myLabel4 = Label(root, text = "Semester").grid(row = 4, column = 0)

text_box = Text(root, height= 10, width = 50).grid(row = 5, column = 0)
submit_button = Button(text = "Submit").grid(row = 6, column = 0)

def submit_click():

    return text_box.get()

def mainloop():

    current_semester += 1
    myLabel4.config(text = f"{current_semester}")

    semester_complete = False
    semester_courses = []
    
    course = submit_click()

    if course == "plan done":
        plan_complete = True
        semester_complete = True
    elif course == "semester done":
        semester_complete = True
    else:
        semester_courses.append(Course(course))

        graduation_plan[current_semester] = semester_courses

root.mainloop()

for semester, courses in graduation_plan.items():

    print(semester)

    for course in courses:

        print(courses)