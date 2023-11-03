import cws
import misc

def creditsTest():
    expected = 3
    output = cws.get_credits("INST326")
    assert(expected == output)
