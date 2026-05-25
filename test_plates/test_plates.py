from plates import is_valid

def test_startnum():
    assert is_valid("12asdf") == False

def test_starttwoletters():
    assert is_valid("a1234") == False

def test_toolong():
    assert is_valid("aadafsaf") == False

def test_correct():
    assert is_valid("AAA222") == True

def test_illchar():
    assert is_valid("AAA 22") == False

def test_nummid():
   assert is_valid("AAA22A") == False


def test_zeroplacement():
   assert is_valid("AAA022") == False
