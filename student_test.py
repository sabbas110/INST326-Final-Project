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


def test_credits():
    course_content = cws.get_course_content('INST326')
    expected = 3
    output = cws.get_credits(course_content)
    assert(expected == output)



def test_corequisite():
    expected = []
    output = cws.get_corequisite("INST326")
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
    expected = ([['MATH140', 'MATH141']], False)
    output = prp.prereq_format1_parser('Prerequisite: MATH140, MATH141')
    assert(expected == output)

def test_prereq2a():
    expected = 'Minimum grade of C- in CMSC141 and MATH140.'
    output = prp.prereq_format2a_parser('CMSC142')
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
    expected = 'CMSC100.'
    output = prp.crosslist_parser('INST101')
    assert(expected == output)

def test_genEdparser():
    expected = ['DSSP']
    output = prp.genEd_parser('INST327')
    assert(expected == output)

def test_courseformat():
    expected = 'INST326'
    output = misc.format_course_name('INST326')
    assert(expected == output)
 

