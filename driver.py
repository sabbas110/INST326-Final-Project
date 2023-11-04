'''
this file is just being used to simulate what running the program is going to be like
don't worry about this file
'''

from bs4 import BeautifulSoup
import requests
from misc import Course

source = requests.get("https://app.testudo.umd.edu/soc/202401/AGST").text

soup = BeautifulSoup(source, "lxml")

courses = soup.find_all("div", class_ = "course-id")

courses_list = []

for course in courses:

    courses_list.append(course.text)

for course in courses_list:

    course = Course(course)
    print(course.name)
    print(course.credits)
    print(course.corequisites)
    print(course.prerequisites)
    print(course.crosslist)
    print(course.genEd)
    
