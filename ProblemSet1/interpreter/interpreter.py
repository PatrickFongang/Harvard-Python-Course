def main():
    exp=input("Expression:")
    print(doTheMath(exp))

def doTheMath(exp):
    exp=exp.split()
    match exp[1]:
        case "+":
            return float(exp[0])+float(exp[2])
        case "/":
            return float(exp[0])/float(exp[2])
        case "-":
            return float(exp[0])-float(exp[2])
        case "*":
            return float(exp[0])*float(exp[2])
        case _:
            return "Unknown operation"


main()

