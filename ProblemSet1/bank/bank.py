def main():
    greeting=input("Greeting: ")
    print(howmuch(greeting))

def howmuch(greeting):
    g=greeting.lower().strip()
    if "hello" in g:
        return "$0"
    elif g[0]=='h':
        return "$20"
    return "$100"

main()
