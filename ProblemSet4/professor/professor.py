import random


def main():
    level=get_level()
    score=0
    for _ in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        for _ in range(3):
            print(x,"+",y,"=",end=" ")
            answer=input()
            if answer.isnumeric()==True and int(answer)==x+y:
                score+=1
                break
            else:
                print("EEE")
        print(x,"+",y,"=",x+y)
    print("Score:",score)

def get_level():
    levels=['1','2','3']
    while True:
        level=input("Level: ")
        if level in levels:
            return int(level)


def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    return random.randint(pow(10,level-1),pow(10,level)-1)


if __name__ == "__main__":
    main()
