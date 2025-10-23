from um import count

def main():
    test_begin()
    test_end()
    test_general()

def test_begin():
    assert count("Um, hello world")==1
    assert count("um, hello world")==1
    assert count("Um... hello world")==1
    assert count("ummm, hello world")==0
def test_end():
    assert count("hello world um.")==1
    assert count("Um, hello world, ummm")==1
    assert count(" hello world. Um")==1
    assert count("hello worldum")==0
    assert count("Hello world,um")==1

def test_general():
    assert count("Um, hello, um... world")==2
    assert count("Um, hello ummm world")==1
    assert count("Um, umhelloum world")==1
    assert count("umumumumum")==0
    assert count("um, um um....um um")==5
    assert count("Um, hello um")==2

if __name__=="__main__":
    main()

