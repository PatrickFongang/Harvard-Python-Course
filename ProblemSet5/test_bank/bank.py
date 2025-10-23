def main():
    greeting=input("Greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    g=greeting.lower().strip()
    if "hello" in g:
        return 0
    elif g[0]=='h':
        return 20
    return 100

if __name__=="__main__":
    main()
