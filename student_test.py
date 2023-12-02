import cws
import misc
import prp

#run it with:
#python -m pytest student_test.py  
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
    
def test_course_content():
    output = cws.get_course_content('INST326')
    #Do multiple subtests with each line being a subtest using .find method
    #Find credits for string output assert(3=output)
    #Find seats: assert(15=output)


def test_credits():
    course_content = cws.get_course_content('INST326')
    expected = 3
    output = cws.get_credits(course_content)
    assert(expected == output)



def test_corequisite():
    course_content = cws.get_corequisite('INST326')
    expected = []
    output = cws.get_corequisite(course_content)
    assert(expected == output)


def test_prerequisite():
    course_content = cws.get_course_content('INST311')
    expected = [['PSYC100', 'SOCY105']]
    output = cws.get_prerequisites(course_content)
    assert(expected == output)

def test_getGenEd():
    course_content = cws.get_course_content('HIST111')
    expected = ['DSHS', 'DVUP']
    output = cws.get_genEd(course_content)
    assert(expected == output)

def test_prereq1():
    expected = [['MATH136', 'MATH140']]
    output = prp.prereq_format1_parser('Prerequisite: 1 course with a minimum grade of C- from (MATH136, MATH140).')
    assert(expected == output)

def test_prereq2a():
    course_content = prp.prereq_format2a_parser('CMSC242')
    expected = 'Minimum grade of C- in CMSC141 and MATH140.'
    output = prp.prereq_format2a_parser(course_content)
    assert(expected == output)

def test_prereq2b():
    expected = 'Minimum grade of C- in CMSC330 and CMSC351; 1 course with a minimum grade of C- from (MATH240, MATH341, MATH461).'
    output = prp.prereq_format2b_parser('CMSC426')
    assert(expected == output)

def test_prereq2c():
    expected = '1 course with a minimum grade of C- from (MATH131, MATH141).'
    output = prp.prereq_format2c_parser('MATH240')
    assert(expected == output)

def test_prereq3():
    expected = 'Minimum grade of C- in INST364.'
    output = prp.prereq_format3_parser('INST467')
    assert(expected == output)

def test_prereqassembler():
    expected = 'Minimum grade of C- from INST126 or GEOG276; and minimum grade of C- in STAT100; and minimum grade of C- in one of the following (AASP101, ANTH210, ANTH260, ECON200, ECON201,GEOG202, GVPT170, PSYC100, SOCY100, or SOCY105).'
    output = prp.prerequisite_assembler('INST366')
    assert(expected == output)

def test_crosslist():
    expected = ['INST101', 'CMSC100']
    output = prp.crosslist_parser('Credit only granted for: INST101, CMSC100')
    assert(expected == output)

def test_genEdparser():
    course_content = prp.genEd_parser('INST327')
    expected = ['DSSP']
    output = prp.genEd_parser(course_content)
    assert(expected == output)

def test_courseformat():
    course_content = misc.format_course_name('INST326')
    expected = 'INST326'
    output = misc.format_course_name(course_content)
    assert(expected == output)
