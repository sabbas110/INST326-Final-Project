import re

#doesnt work for this one yet
# straightforward one or more courses format
# #Prerequisite: MATH240, MATH241

def prereq_format1_parser(prereq_description):
    prereqs = prereq_description.replace("Prerequisite: ", "")
    prereqs = prereqs.replace("and ", "").replace(",", "").split()
    return prereqs


# 1 course with minumum grade of C- from... format

def prereq_format2a_parser(prereq_description):
    prereq = re.search(r'(?<=from \().*(?=\))', prereq_description).group().split(", ")
    return prereq

# 1 course with minumum grade of C- from... format

def prereq_format2b_parser(prereq_description):
    prereq = re.search(r'(?<=from ).*', prereq_description).group()
    andFlag = False
    if "and" in prereq:
        andFlag = True
    prereq = prereq.replace("or ", "").replace("and ", "").replace(",", "").split(" ")
    return prereq, andFlag


# minimum grade of C- in... format

def prereq_format3_parser(prereq_description):
    prereq = re.search(r'(?<=C- in ).*', prereq_description).group()
    andFlag = False
    if "and" in prereq:
        andFlag = True
    prereq = prereq.replace("or ", "").replace("and ", "").replace(",", "").split(" ")
    return prereq, andFlag


'''
prereq list assembler
'''

def prerequisite_assembler(prerequisites):
    assembled_prerequisites = []

    for prereq in prerequisites:
        print(prereq)

        '''
        these conditionals search for substrings within the unassembled prerequisites

        if a condition is met, there is an associated parser function that will handle
        the prerequisite that contains a specific substring
        '''
        if "C- from (" in prereq:

            parsed_prereq = prereq_format2a_parser(prereq)
            assembled_prerequisites.append(parsed_prereq)

        elif "C- from " in prereq:

            parsed_prereq, andFlag = prereq_format2b_parser(prereq)

            # if the andFlag is true, that means the courses should be entered seperately because they are all required
            # if there is only 1 course then it can just be entered seperately
            if andFlag == True or len(parsed_prereq) == 1:
                for prereq in parsed_prereq:
                    assembled_prerequisites.append(prereq)
            # if the flag is false then that means any one of those classes suffice, so they should be entered together in a list
            else:
                assembled_prerequisites.append(parsed_prereq)

        elif "C- in" in prereq:

            parsed_prereq, andFlag = prereq_format3_parser(prereq)
            print(andFlag)

            # if the andFlag is true, that means the courses should be entered seperately because they are all required
            # if there is only 1 course then it can just be entered seperately
            if andFlag == True or len(parsed_prereq) == 1:
                for prereq in parsed_prereq:
                    assembled_prerequisites.append(prereq)
            # if the flag is false then that means any one of those classes suffice, so they should be entered together in a list
            else:
                assembled_prerequisites.append(parsed_prereq)

        elif prereq.startswith("Prerequisite"):

            parsed_prereq = prereq_format1_parser(prereq)

            for prereq in parsed_prereq:
                assembled_prerequisites.append(prereq)

    #return the list of assembled prerequisites after all iterations of prerequisites
    return assembled_prerequisites

'''
Crosslist parser
'''

def crosslist_parser(script):
    script = script.replace("Credit only granted for: ", "")
    script = script.replace(",", "").replace("and ", "").replace("or ", "")
    crosslist = script.split()
    return crosslist
