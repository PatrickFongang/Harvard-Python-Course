def main():
    output=shorten(input("Input: "))
    print(f"Output: {output}")

def shorten(word):
    vowels=['a','e','i','o','u']
    output=""
    for char in word:
        if char.lower() in vowels:
            continue
        output+=char
    return output

if __name__=="__main__":
    main()
