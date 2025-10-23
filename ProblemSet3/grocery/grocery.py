def main():
    list=make_list()
    keys=sorted(list)
    for item in keys:
        print(list[item],item.upper())

def make_list():
    grocery_list={}

    while True:
        try:
            item=input().strip().lower()
        except EOFError:
            print()
            return grocery_list
        if item in grocery_list.keys():
            grocery_list[item]+=1
        else:
            grocery_list[item]=1

main()
