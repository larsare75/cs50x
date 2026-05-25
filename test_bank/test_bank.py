from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("howdy") == 20
    
def test_nohello():
    assert value("what a nice day") == 100

def test_helloCAP():
    assert value("HELLO") == 0

def test_hCAP():
    assert value("HOWDY") == 20
    
def test_nohelloCAP():
    assert value("WHAT A NICE DAY") == 100
