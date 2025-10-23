import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match=re.search(r"^(\d*)\.(\d*)\.(\d*)\.(\d*)$",ip)
    if not match:
        return False
    for group in match.groups():
        if not group.isnumeric() or int(group)>255 or (group[0]=='0' and len(group)!=1):
            return False
    return True





if __name__ == "__main__":
    main()
