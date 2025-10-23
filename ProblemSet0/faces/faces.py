def main():
    text=input()
    print(convert(text))

def convert(str):
    str=str.replace(":)","🙂")
    return str.replace(":(","🙁")

main()
