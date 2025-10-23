import re
def main():
    year,month,day=get_date()
    print(f"{year}-{month:02}-{day:02}")

def get_date():
    while True:
        try:
            date=input("Date: ").strip().lower()
            month,day,year=date.split("/")
            if month.isnumeric()==False:
                continue
        except ValueError:
            try:
                month,rest=date.split(" ",1)
                day,year=rest.split(", ")
            except ValueError:
                continue
        if check_year(year) and check_month(month) and check_day(day):
            return (int(year),check_month(month),int(day))

def check_year(y):
    return y.isnumeric() and int(y)<10000

def check_month(m):
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    if m.title() in months:
        return months.index(m.title())+1
    elif m.isnumeric() and int(m)<=12:
        return int(m)
    else:
         return False

def check_day(d):
    return d.isnumeric() and int(d)<=31

main()
