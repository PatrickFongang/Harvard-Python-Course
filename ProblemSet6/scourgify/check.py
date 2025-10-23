import sys

def check_command(command):
    if len(command)>3:
        sys.exit("Too many command-line arguments")
    elif len(command)<3:
        sys.exit("Too few command-line arguments")
    elif command[2][len(command[2])-4:]!=".csv":
        sys.exit(f"Could not read {command[2]}")
    elif command[1][len(command[1])-4:]!=".csv":
        sys.exit(f"Could not read {command[1]}")
    else:
        try:
            open(command[1])
        except FileNotFoundError:
            sys.exit(f"File {command[1]} does not exist")
