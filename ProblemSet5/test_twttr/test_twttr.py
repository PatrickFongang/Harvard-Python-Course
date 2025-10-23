from twttr import shorten
def main():
    test_twttr()

def test_twttr():
    assert shorten("AEIOU")==""
    assert shorten("aeiou")==""
    assert shorten("AtEwittOru")=="twttr"
    assert shorten("1234")=="1234"
    assert shorten(".,;/")==".,;/"

if __name__=="__main__":
    main()
