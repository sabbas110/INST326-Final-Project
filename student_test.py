import cws
import misc

#run it with:
#python3 -m pytest StudentTests.py  
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

def creditsTest():
    expected = 3
    output = cws.get_credits("INST326")
    assert(expected == output)

def corequisiteTest():
    expected = []
    output = cws.get_corequisite("INST326")
    assert(expected == output)

def prerequisiteTest():
    expected = [[INST201, PSYC100, SOCY105]]
    output = cws.get_prerequisites('INST371')
    assert(expected == output)

def getGenEdTest():
    expected = ['DSHS', 'DVUP']
    output = cws.get_genEd('HIST111')
    assert(expected == output)
