from um import count
#import pytest

def test_conv():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2
    
#def test_wronginput():   
#    with pytest.raises(ValueError):
#        convert("9:60 AM to 5:60 PM") 
