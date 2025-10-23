import random

def main():
    n=get_n()
    rand=random.randint(1,n)
    while True:
        try:
            guess=int(input("Guess: "))
        except ValueError:
            continue
        if guess<1:
            continue
        if guess>rand:
            print("Too large!")
        elif guess<rand:
            print("Too small!")
        else:
            print("Just right!")
            break

def get_n():
    while True:
        n=input("Level: ")
        if n.isnumeric()==False:
            continue
        return int(n)

main()
