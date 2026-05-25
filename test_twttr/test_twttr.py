from twttr import shorten

def test_plain():
    assert shorten("twitter") == "twttr"

def test_number():
    assert shorten("twi6tter") == "tw6ttr"
    
def test_capcons():
    assert shorten("twiTTer") == "twTTr"

def test_vow():
    assert shorten("twItter") == "twttr"

def test_punct():
   assert shorten("twitt.er") == "twtt.r"
