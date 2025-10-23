import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern=r"^(1[0-2]|[0-9])(?:\:([0-5][0-9]))? (AM|PM) to (1[0-2]|[0-9])(?:\:([0-5][0-9]))? (AM|PM)$"
    match=re.search(pattern,s)
    if not match:
        raise ValueError("Wrong input")
    
    hour1,minute1,hour2,minute2=[int(match.group(1)),match.group(2) or 0,int(match.group(4)),match.group(5) or 0]

    hour1-=12*(match.group(3)=="AM") if hour1==12 else (-1)*12*(match.group(3)=="PM")
    hour2-=12*(match.group(6)=="AM") if hour2==12 else (-1)*12*int(match.group(6)=="PM")

    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"


if __name__ == "__main__":
    main()
