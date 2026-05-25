from tull2 import  cleaninput

def testvanlig():
    assert cleaninput("Lars") == "hello, Lars"


def testkomma():
    assert cleaninput("Malan,David") == "hello, David Malan"
