from webscrapers import get_corequisite, get_credits, get_crosslist, get_prerequisites, get_genEd

class Course:
    '''Creates a University of Maryland course.
    Attributes:
        name(str): name of the course as it appears on the Schedule of Classes.
        credits(int): number of credit hours the class is worth.
        prerequisites(list): list of prerequisite courses associated with course.
        corequisites(list): list of prerequisite courses associated with course.
        crosslist(list): list of courses that associated course grants credit for in addition to itself.
        genEd(list): list of general education requirements the course satisfies.
    '''

    def __init__(self, name):
        self.name = format_course_name(name)
        self.credits = get_credits(self.name)
        self.prerequisites = get_prerequisites(self.name)
        self.corequisites = get_corequisite(self.name)
        self.crosslist = get_crosslist(self.name)
        self.genEd = get_genEd(self.name)


def format_course_name(course_in):
    '''Formats a course name by the style standard that appears in the Schedule of Classes.
    Args:
        Course_in(str): name of a course
    Returns:
        Formatted_course_name(str): course name adhered to style standard of courses in the Schedule of Classes
    '''
    #retreiving and formatting the department portion of the course_in (the first 4 characters, ex: INST)
    department = (course_in[:4]).upper()

    #formatting course_in to be congruent with formatting of course names on website
    formatted_course_name = department + course_in[4:]

    return formatted_course_name

course = Course("gems104")
print(course.genEd)
