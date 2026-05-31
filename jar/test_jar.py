from jar import Jar
import pytest

def test_init():
    assert isinstance(Jar(),Jar) == True
    assert isinstance(Jar(5),Jar) == True
    assert isinstance(Jar(0),Jar) == True
    with pytest.raises(ValueError):
        jar=Jar("cat")
    with pytest.raises(ValueError):
        jar=Jar(-5)
    


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    jar.deposit(1)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.deposit(10)
    



def test_withdraw():
    jar=Jar()
    jar.deposit(10)
    jar.withdraw(5)
    jar.withdraw(2)
    with pytest.raises(ValueError):
        jar.withdraw(5)
    jar.withdraw(3)
    
def test_decor():
    jar=Jar()
    jar.deposit(10)
    assert jar.size == 10
    assert jar.capacity == 12