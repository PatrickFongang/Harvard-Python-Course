def main():
    names=get_names()
    text="Adieu, adieu, to "+names[0]
    if len(names)>1:
        for name in names[1:len(names)-1]:
            text+=", "+name
        if len(names)>2:
            text+=","
        print(text+" and "+names[len(names)-1])
    else:
        print(text)

def get_names():
    names=[]
    while True:
        try:
            names.append(input("Name: ").strip())
        except EOFError:
            print()
            return names

main()


