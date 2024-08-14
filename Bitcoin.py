#Expects the user to specify as a command-line argument the number of Bitcoins, n that they would like to buy.
#If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
#Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
#which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
#Be sure to catch any exceptions, as with code like:
#Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.

#Import libraries

import requests
import sys

def main():
    # Get user input
    if len(sys.argv) != 2:
        sys.exit("Invalid input")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Not a valid input")

    # Query the API for the CoinDesk Bitcoin Price Index
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        x = response.json()
        rate = x["bpi"]["USD"]["rate_float"]
        usd_amount = amount * rate
        print(f"${usd_amount:,.4f}")

    except requests.RequestException:
        sys.exit("Not a valid input")

if __name__ == '__main__':
    main()
