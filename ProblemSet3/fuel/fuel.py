def main():
    percent=round(get_fraction()*100)
    if percent<=1:
        print("E")
    elif percent>=99:
        print("F")
    else:
        print(f"{percent}%")

def get_fraction():
    while True:
        try:
            text=input("Fraction: ")
            if text.find("/")==-1:
                continue
            x,y=text.split("/")
            if x.isnumeric()==False or y.isnumeric()==False or int(x)>int(y):
                continue
            return int(x)/int(y)
        except ValueError and ZeroDivisionError:
            pass

main()
