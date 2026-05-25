from tull import checkmail

def test_vanlig():
    assert checkmail("larskillingdalen@gmail.edu")=="Valid"
def test_upper():
    assert checkmail("larskillingdalen@gmail.EDU")=="Valid"
def test_com():
    assert checkmail("larskillingdalen@gmail.com")=="Valid"
def test_no():
    assert checkmail("larskillingdalen@gmail.no")=="Invalid"
def test_vanlig():
    assert checkmail("larskillingdalen@gmail.edu")=="Valid"
def test_vanlig():
    assert checkmail("malan@cs50.harvard.edu")=="Valid"



