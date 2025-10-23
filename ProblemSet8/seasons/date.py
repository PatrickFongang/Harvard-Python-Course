import sys

def check_date(d):
    try:
        year,month,day=d.split("-")
    except ValueError:
        sys.exit("Wrong input")
    if check_year(year) and check_month(month) and check_day(day):
        return True
    else:
        sys.exit("Wrong input")


def check_year(y):
    return y.isnumeric() and int(y)<10000

def check_month(m):
    if m.isnumeric() and len(m)==2 and int(m)<=12:
        return int(m)
    else:
         return False

def check_day(d):
    return d.isnumeric() and len(d)==2 and int(d)<=31

