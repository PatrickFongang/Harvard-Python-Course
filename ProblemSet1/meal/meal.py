def main():
    text=input("What time is it? ").strip()
    if text.find("a.m.")!=-1 or text.find("p.m.")!=-1:
        text=text.split()
        time=convert(text[0])+convertTo24h(text[1])
    else:
        time=convert(text)
    if 7.0<=time and time<=8.0:
        print("breakfast time")
    if 12.0<=time and time<=13.0:
            print("lunch time")
    if 18<=time and time<=19:
            print("dinner time")

def convert(time):
    colon=time.find(':')
    return float(time[:colon])+float(time[colon+1:])/60.0

def convertTo24h(add12):
     if add12=="a.m.":
        return 0
     return 12

if __name__ == "__main__":
    main()
