from seasons import check_birthdate


def testdato():
    assert check_birthdate("0001-01-01")==True
    assert check_birthdate("1994-09-09")==True 
    assert check_birthdate("2010-10-10")==True 
    assert check_birthdate("1998-11-19")==True 
    assert check_birthdate("1987-03-20")==True 
    assert check_birthdate("1999-09-29")==True 
    assert check_birthdate("1999-12-30")==True 
    assert check_birthdate("1999-12-31")==True 


def testdatowrong():
    assert check_birthdate("1999-99-00")==False 
    assert check_birthdate("1999-00-99")==False 
