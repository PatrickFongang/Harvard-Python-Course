import requests
import sys
import json

def main():
    bitcoins=how_much()
    value=get_value()
    print(f"${(bitcoins*value):,.4f}")

def how_much():
    try:
        buy=sys.argv[1]
    except IndexError:
        sys.exit("Missing command-line argument")
    try:
        return float(buy)
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_value():
    response=requests.get(f"https://rest.coincap.io/v3/assets/{sys.argv[2].strip().lower()}?apiKey=9f61ecef01f9076f629a64ea62ce377cc0ea8f2c3fecfae739f887f1d180df0a")
    content=response.json()
    return float(content["data"]["priceUsd"])

main()
