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

def test_prereq1a():
    expected = (['INST327'], False)
    output = prp.prereq_format1_parser('Prerequisite: INST327')
    assert(expected == output)

def test_prereq1b():
    expected = (['MATH115'], False)
    output = prp.prereq_format1_parser('Prerequisite: MATH115')
    assert(expected == output)

def test_prereq2ai():
    expected = ['INST201', 'INST301']
    output = prp.prereq_format2a_parser('Prerequisite: 1 course with a minimum grade of C- from (INST201, INST301)')
    assert(expected == output)
    
def test_prereq2aii():
    expected = ['INST126', 'GEOG276']
    output = prp.prereq_format2a_parser('Prerequisite: 1 course with a minimum grade of C- from (INST126, GEOG276)')
    assert(expected == output)

def test_prereq2bi():
    expected = (['INST362', 'INST367'], False)
    output = prp.prereq_format2b_parser('Prerequisite: Minimum grade of C- from INST362 or INST367')
    assert(expected == output)

#Failed, need to fix
'''def test_prereq2bii():
    expected = (['PSYC100', 'SOCY105'], False)
    output = prp.prereq_format2b_parser('Prerequisite: Minimum grade of C- in PSYC100 or SOCY105')
    assert(expected == output)
'''
def test_prereq2ci():
    expected = (['ENEE467', 'CMSC420'], False)
    output = prp.prereq_format2c_parser('and (ENEE467 or CMSC420)')
    assert(expected == output)

def test_prereq2cii():
    expected = (['INST326', 'BSOS326', 'GEOG376'], False)
    output = prp.prereq_format2c_parser('and (INST326, BSOS326, or GEOG376)')
    assert(expected == output)

def test_prereq3a():
    expected = (['INST364'], False)
    output = prp.prereq_format3_parser('Minimum grade of C- in INST364')
    assert(expected == output)

def test_prereq3b():
    expected = (['INST380'], False)
    output = prp.prereq_format3_parser('Minimum grade of C- in INST380')
    assert(expected == output)
    
def test_prereq4a():
    expected = ['INST201', 'INST301', 'BSOS233']
    output = prp.prereq_format4_parser('minimum grade of a C- from one of the following (INST201, INST301, or BSOS233)')
    assert(expected == output)

def test_prereq4b():
    expected = ['BSOS331', 'GEOG273', 'INST326']
    output = prp.prereq_format4_parser('minimum grade of C- from one of the following (BSOS331, GEOG273, or INST326)')
    assert(expected == output)

def test_prereqassemblera():
    expected = [['INST201', 'INST301'], 'INST314', 'PSYC100']
    output = prp.prerequisite_assembler(['Prerequisite: Minimum grade of C- from INST201 or INST301', 'and minimum grade of C- in INST314 and PSYC100'])
    assert(expected == output)

def test_prereqassemblerb():
    expected = [['INST201', 'INST301'], ['PSYC100', 'SOCY105'], 'INST326', 'STAT100']
    output = prp.prerequisite_assembler(['Prerequisite: Minimum grade of C- from INST201 or INST301',  'and minimum grade of C- from PSYC100 or SOCY105', 'and minimum grade of C- in INST326 and STAT100'])
    assert(expected == output)
    
def test_crosslista():
    expected = ['INST101', 'CMSC100']
    output = prp.crosslist_parser('Credit only granted for: INST101, CMSC100')
    assert(expected == output)

def test_crosslistb():
    expected = ['INFM289I', 'INST155']
    output = prp.crosslist_parser('Credit only granted for: INFM289I, INST155')
    assert(expected == output)
    
def test_courseformata():
    course_content = misc.format_course_name('INST326')
    expected = 'INST326'
    output = misc.format_course_name(course_content)
    assert(expected == output)

def test_courseformatb():
    course_content = misc.format_course_name('CMSC131')
    expected = 'CMSC131'
    output = misc.format_course_name(course_content)
    assert(expected == output)

'''from misc import Course
import ver

graduation_plan = {
    0: [Course("STAT100")],
    1: [Course("MATH115"), Course("MATH113"), Course("ENGL101"), Course("JOUR200"), Course("AASP200")],
    2: [Course("INST126"), Course("PSYC100"), Course("RDEV250"), Course("COMM107"), Course("THET116")],
    3: [Course("INST201"), Course("INST326"), Course("INST311"), Course("BSCI135"), Course("ANSC101")],
    4: [Course("INST327"), Course("INST335"), Course("ENGL290"), Course("AMST202"), Course("KNES265")],
    5: [Course("INST314"), Course("INST364"), Course("ENGL394"), Course("AGST333"), Course("AGST426")],
    6: [Course("INST352"), Course("INST341"), Course("WGSS263"), Course("EDSP210"), Course("GEOG272")],
    7: [Course("INST346"), Course("INST362"), Course("INST366"), Course("AREC365"), Course("COMM230")],
    8: [Course("INST490"), Course("INST464"), Course("inst408i"), Course("COMM250"), Course("ECON185")],
}


graduation_plan2 = {
    0: [Course("STAT100")],
    1: [Course("MATH115"), Course("MATH113"), Course("ENGL101"), Course("JOUR200"), Course("AASP200"), Course("INST126")],
    2: [Course("PSYC100"), Course("RDEV250"), Course("COMM107"), Course("THET116"), Course("CMSC131")],
    3: [Course("INST201"), Course("INST326"), Course("INST311"), Course("BSCI135"), Course("ANSC101")],
    4: [Course("INST327"), Course("ENGL290"), Course("AMST202"), Course("KNES265")],
    5: [Course("HIST111"), Course("INST364"), Course("ENGL394"), Course("AGST333"), Course("AGST426")],
    6: [Course("INST352"), Course("INST341"), Course("WGSS263"), Course("EDSP210"), Course("GEOG272")],
    7: [Course("INST346"), Course("INST362"), Course("INST366"), Course("AREC365"), Course("COMM230")],
    8: [Course("INST490"), Course("INST464"), Course("inst408i")],
}


#Passed 
def test_verify_credit():
    expected = (True, 'Satisfied')
    output = ver.verify_credits(graduation_plan)
    assert(output==expected)

def test_verify_genEd():
    expected = (True, 'Satisfied')
    output = ver.verify_genEd(graduation_plan)
    assert(output==expected)

def test_verify_prerequisite():
    expected = (True, 'Satisfied')
    output = ver.verify_prerequisite(graduation_plan)
    assert(output==expected)    

def test_verify_corequisite():
    expected = (True, 'Satisfied')
    output = ver.verify_corequisite(graduation_plan)
    assert(output==expected) 
    
def test_verify_major_requirements():
    expected = (True, 'Satisfied')
    output = ver.verify_major_requirements('Information Science', graduation_plan)
    assert(output==expected) 

#Failed
def test_verify_credit():
    expected = (False, 'Your graduation plan is 1 credits under the 120 credit minimum')
    output = ver.verify_credits(graduation_plan2)
    assert(output==expected)

def test_verify_genEd():
    expected = (False, '3 more credits are needed to satisfy DSHU\n2 more credits are needed to satisfy SCIS\n')
    output = ver.verify_genEd(graduation_plan2)
    assert(output==expected)

def test_verify_prerequisite():
    expected = (False, 'Satisfied')
    output = ver.verify_prerequisite(graduation_plan2)
    assert(output==expected)    


def test_verify_corequisite():
    expected = (False, 'Need to be taking or have already completed MATH140 in order to take CMSC131\n')
    output = ver.verify_corequisite(graduation_plan2)
    assert(output==expected) 
    
def test_verify_major_requirements():
    expected = (False, 'Missing the following major requirements:\nINST314\nINST335\n')
    output = ver.verify_major_requirements('Information Science', graduation_plan2)
    assert(output==expected) 
'''
