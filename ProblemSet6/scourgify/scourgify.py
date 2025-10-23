import csv
import sys
from check import check_command

def main():
    check_command(sys.argv)
    with open(sys.argv[1],newline="") as file1:
        with open(sys.argv[2],"w",newline="") as file2:
            reader=csv.DictReader(file1)
            writer=csv.DictWriter(file2,fieldnames=["first","last","house"])
            writer.writeheader()
            for row in reader:
                last,first=row["name"].split(", ")
                house=row["house"]
                writer.writerow({"first":first,"last":last,"house":house})

main()
