from twitter import extract

def test_tweet():
    assert extract("https://twitter.com/lars") =="lars"