import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern=r"<iframe.* src=\"https?://(?:www\.)?youtube\.com/embed/([^\"]+)"
    match=re.search(pattern,s)
    if match:
        return ("https://youtu.be/"+match.group(1)).replace("embed/","")
    return


if __name__ == "__main__":
    main()
