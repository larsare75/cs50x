from fuel import convert
from fuel import gauge
import pytest

def test_converttostring():
    assert convert("1/4") == 25

def test_gaugesignisthere():
    assert gauge(25) == "25%"

def test_valueerror():
    with pytest.raises(ValueError):
        convert("1/2.2") 

def test_valueerror2():
    with pytest.raises(ValueError):
        convert ("-1/2") 

def test_zerodiv():
    with pytest.raises(ZeroDivisionError):
        convert ("1/0") 


def test_correct1():
    assert gauge(1) == "E"

def test_correct99():
    assert gauge(99) == "F"


#def test_illchar():
#    assert is_valid("AAA 22") == False

#def test_nummid():
#   assert is_valid("AAA22A") == False


#def test_zeroplacement():
#   assert is_valid("AAA022") == False
