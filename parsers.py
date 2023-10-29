import re

# straightforward one or more courses format
s1a = "CCJS100"
s1b = "MATH140 and MATH141"
s1c = "INST326, INST327, and INST314"

def prereq_format1_parser(prereq_description):
    prereq = prereq_description.replace("and ", "").replace(",", "").split()
    return prereq


# 1 course with minumum grade of C- from... format
s2 = "1 course with a minimum grade of C- from (MATH461, MATH240, MATH341)."

def prereq_format2_parser(prereq_description):
    prereq = re.search(r'(?<=from \().*(?=\))', prereq_description).group().split(", ")
    return prereq


# minimum grade of C- in... format
s3a = "and minimum grade of C- in MATH310."
s3b = "and minimum grade of C- in MATH310 or MATH241;"

def prereq_format3_parser(prereq_description):
    prereq = re.search(r'(?<=C- in ).*(?=[;.])', prereq_description).group().split(" or ")
    return prereq



'''
Crosslist parser
'''

def crosslist_parser(script):
    script = script.replace("Credit only granted for: ", "")
    script = script.replace(",", "").replace("and ", "").replace("or ", "")
    crosslist = script.split()
    return crosslist