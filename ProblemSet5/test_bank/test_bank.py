from bank import value

def main():
    value("Hey david")

def test_bank():
    assert value("Hello")==0
    assert value("hello, David")==0
    assert value("help me")==20
    assert value("Good Mornig David")==100
    assert value("whats up David")==100

if __name__=="__main__":
    main()

