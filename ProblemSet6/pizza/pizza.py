import sys
import csv
from tabulate import tabulate

def main():
    check_command()
    print_table()

def check_command():
    command=sys.argv
    if len(command)>2:
        sys.exit("Too many command-line arguments")
    elif len(command)<2:
        sys.exit("Too few command-line arguments")
    elif command[1][len(command[1])-4:]!=".csv":
        sys.exit("Not a CSV file")
    else:
        try:
            open(command[1])
        except FileNotFoundError:
            sys.exit("File does not exist")

def print_table():
    l=[]
    with open(sys.argv[1]) as file:
        reader=csv.reader(file)
        for line in reader:
            l.append(line)
        print(tabulate(l[1:],headers=l[0],tablefmt="grid"))

if __name__=="__main__":
    main()
