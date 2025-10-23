from numb3rs import validate

def main():
    test_numbers()
    test_format

def test_numbers():
    assert validate("1.3.23.3")==True
    assert validate("0.0.0.0")==True
    assert validate("01.3.23.3")==False
    assert validate("12323.3.23.3")==False
    assert validate("23.324234.32.3")==False
    assert validate("1.-3.23.3")==False

def test_format():
    assert validate("1.3.23.3")==True
    assert validate("1,3.23.3")==False
    assert validate("13.23.3")==False
    assert validate("1.3.23.3.2")==False
    assert validate(".1.-3.23.3.")==False
    assert validate("cat")==False

if __name__=="__main__":
    main()
