from pyfiglet import Figlet
import sys
import random

figlet=Figlet()

def main():
    if check()==True:
        if len(sys.argv)==1:
            f=random.choice(figlet.getFonts())
            figlet.setFont(font=f)
        else:
            figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
    text=input("Input: ")
    print("Output:")
    print(figlet.renderText(text))

def check():
    if len(sys.argv)==1:
        return True
    if len(sys.argv)!=3:
        return False
    if sys.argv[1]!="-f" and sys.argv[1]!="--font":
        return False
    if sys.argv[2].lower().strip() not in figlet.getFonts():
        return False
    return True

main()
