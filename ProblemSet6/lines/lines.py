import sys

def main():
    check_command()
    print(count_lines(sys.argv[1]))

def check_command():
    try:
        file=sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")
    if file[len(file)-3:]!=".py":
        sys.exit("Not a python file")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    try:
        open(file)
    except FileNotFoundError:
        sys.exit("File does not exist")

def count_lines(f):
    count=0
    with open(f,"r") as file:
        for line in file:
            if line.lstrip().startswith("#") or not line.strip():
                continue
            count+=1
    return count

if __name__=="__main__":
    main()
