import cws
import misc
import prp

#run it with:
#python3 -m pytest student_test.py  
'''
heres the idea:

def whatever-function-you're-testingTest()
    expected = what the correct result should be
    output = function-name(whatever you wanna test as a parameter)
    assert(expect == output)


examples (they dont work theyre just examples):

def get_crosslistTest():
    expected = [CCJS100, CCJS101]
    output = get_crosslist("CCJS100")
    assert(expect == output)

*some functions return more than 1 thing like the parsers; they return a list and a flag(boolean).
*youll have to do something like:
    expected flag = False
    expected output = [INST121, INST362]
    output, flag = prereq1formatter("1 course with a minimum grade of C- from (INST121, INST326)")
    assert(output == expected output)
    assert(flag == expected flag)
'''

#We can hardcode everything in the test cases except the output statement
def test_get_course_content():
    output = cws.get_course_content('INST326')

    #Do multiple subtests with each line being a subtest using .find method
    #Find credits for string output assert(3=output)
    #Find seats: assert(15=output)   
def test_credits():
    course_content = cws.get_course_content('INST326')
    expected = 3
    output = cws.get_credits(course_content)
    assert(expected == output)
    #test a class that has 4 credits, or 2 or 1, add new test_credits2 method

def test_credits_2():
    course_content = cws.get_course_content('INST101')
    expected = 1
    output = cws.get_credits(course_content)
    assert(expected == output)

def test_corequisite():
    course_content = cws.get_course_content('INST326')
    expected = []
    output = cws.get_corequisite(course_content)
    assert(expected == output)

def test_corequisite_2():
    course_content = cws.get_course_content('CMSC131')
    expected = ['MATH140']
    output = cws.get_corequisite(course_content)
    assert(expected == output)


def test_prerequisite():
    course_content = cws.get_course_content('INST311')
    expected = [['PSYC100', 'SOCY105']]
    output = cws.get_prerequisites(course_content)
    assert(expected == output)

def test_prerequisite_2():
    course_content = cws.get_course_content('INST346')
    expected = [['INST201', 'INST301'],'INST326', 'INST327']
    output = cws.get_prerequisites(course_content)
    assert(expected == output)

def test_getGenEd():
    course_content = cws.get_course_content('HIST111')
    expected = ['DSHS', 'DVUP']
    output = cws.get_genEd(course_content)
    assert(expected == output)

def test_getGenEd_2():
    course_content = cws.get_course_content('AASP101')
    expected = ['DSHS']
    output = cws.get_genEd(course_content)
    assert(expected == output)


def test_prereq1():
    expected = (['INST327'], False)
    output = prp.prereq_format1_parser('Prerequisite: INST327')
    assert(expected == output)

def test_prereq2a():
    expected = ['INST201', 'INST301']
    output = prp.prereq_format2a_parser('Prerequisite: 1 course with a minimum grade of C- from (INST201, INST301)')
    assert(expected == output)

def test_prereq2b():
    expected = (['INST362', 'INST367'], False)
    output = prp.prereq_format2b_parser('Prerequisite: Minimum grade of C- from INST362 or INST367')
    assert(expected == output)

def test_prereq2c():
    expected = (['ENEE467', 'CMSC420'], False)
    output = prp.prereq_format2c_parser('and (ENEE467 or CMSC420)')
    assert(expected == output)

def test_prereq3():
    expected = (['INST364'], False)
    output = prp.prereq_format3_parser('Minimum grade of C- in INST364')
    assert(expected == output)

def test_prereq4():
    expected = ['INST201', 'INST301', 'BSOS233']
    output = prp.prereq_format4_parser('minimum grade of a C- from one of the following (INST201, INST301, or BSOS233)')
    assert(expected == output)

def test_prereqassembler():
    expected = [['INST201', 'INST301'], 'INST314', 'PSYC100']
    output = prp.prerequisite_assembler(['Prerequisite: Minimum grade of C- from INST201 or INST301', 'and minimum grade of C- in INST314 and PSYC100'])
    assert(expected == output)

def test_crosslist():
    expected = ['INST101', 'CMSC100']
    output = prp.crosslist_parser('Credit only granted for: INST101, CMSC100')
    assert(expected == output)

def test_courseformat():
    course_content = misc.format_course_name('INST326')
    expected = 'INST326'
    output = misc.format_course_name(course_content)
    assert(expected == output)
