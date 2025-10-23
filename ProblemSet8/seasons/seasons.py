from datetime import date,datetime
from num2words import num2words
from date import check_date

def main():
    bday=input("Date of Birth: ")
    check_date(bday)
    today=date.today()
    minutes=get_minutes(datetime.strptime(bday,"%Y-%m-%d").date(),today)
    print(num2words(minutes).capitalize()+" minutes")

def get_minutes(d1,d2):
    delta=d2-d1
    return delta.days*24*60

if __name__=="__main__":
    main()
