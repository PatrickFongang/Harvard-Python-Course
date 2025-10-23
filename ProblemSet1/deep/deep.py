def main():
    text=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    if isok(text):
        print("Yes")
    else:
        print("No")

def isok(text):
    citext=text.lower().strip()
    return citext=="42" or citext=="forty-two" or citext=="forty two"

main()
