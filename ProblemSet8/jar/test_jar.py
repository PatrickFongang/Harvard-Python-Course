from jar import Jar
import pytest

def main():
    test_init()
    test_deposit()
    test_withdraw()
    test_str()

def test_init():
    tests=[-2,-19,-2,-3,"cat","five"]
    for test in tests:
        with pytest.raises(ValueError):
            Jar(test)
def test_deposit():
    jar=Jar()
    jar.size=6
    tests=[-4,-21,"five",7,24,23.2,123]
    for test in tests:
        with pytest.raises(ValueError):
            jar.deposit(test)
    jar.deposit(5)
    assert jar.size==11

def test_withdraw():
    jar=Jar()
    jar.size=6
    tests=[-4,-21,"five",7,24,23.2,123]
    for test in tests:
        with pytest.raises(ValueError):
            jar.withdraw(test)
    jar.withdraw(5)
    assert jar.size==1

def test_str():
    jar=Jar()
    tests=[2,4,5,0,12]
    for test in tests:
        jar.size=test
        assert str(jar)=="🍪"*test

if __name__=="__main__":
    main()
