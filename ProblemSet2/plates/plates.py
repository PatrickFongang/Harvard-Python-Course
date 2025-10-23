def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>6 or len(s)<2:
        return False
    for char in range (len(s)):
        if s[char].isnumeric():
            if(s[:char].isalpha()==False or s[char+1:].isnumeric()==False or s[char]=='0'):
                return False
            return True
    return s.isalpha()

main()
