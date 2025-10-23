from working import convert
import pytest

def main():
    test_format()
    test_minutes()
    test_hours()

def test_format():
    tests=["12;24 am to 6:04 PM","12:24 AM - 6:04 PM","12:24 AM to 6:04 ","12:24 AM TO 6:04 PM"]
    for test in tests:
        with pytest.raises(ValueError):
            convert(test)
    assert convert("6:24 AM to 6:04 PM")=="06:24 to 18:04"

def test_minutes():
    tests=["12:60 AM to 6:04 PM","12:5 AM to 6:004 PM","12:003 AM to 6:04 PM","12: AM to 6:60 PM"]
    for test in tests:
        with pytest.raises(ValueError):
            convert(test)
    assert convert("6:24 AM to 6:04 PM")=="06:24 to 18:04"

def test_hours():
    tests=["13:24 AM to 6:04 PM","06:24 AM to 6:04 PM","24:04 AM to 6:04 PM","00:24 AM to 6:04 PM"]
    for test in tests:
        with pytest.raises(ValueError):
            convert(test)
    assert convert("12:24 AM to 6:04 PM")=="00:24 to 18:04"

if __name__=="__main__":
    main()
