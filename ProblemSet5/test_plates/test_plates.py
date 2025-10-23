from plates import is_valid

def main():
    test_plates()

def test_plates():
    assert is_valid("AAA")==True
    assert is_valid("12AAA")==False
    assert is_valid("AAAAAA")==True
    assert is_valid("AAA23A")==False
    assert is_valid("AAA23423")==False
    assert is_valid("A")==False
    assert is_valid("123134")==False
    assert is_valid("AAA103")==True
    assert is_valid("AA.B 23")==False
    assert is_valid("AAA023")==False
    assert is_valid("AAA22A")==False


if __name__=="__main__":
    main()
