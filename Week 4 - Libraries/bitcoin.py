import sys
import requests
import json

def main():
    data, amount = getData()
    usdValue = data["bpi"]["USD"]["rate_float"]
    ans = float(f"{(usdValue * amount):.4f}")
    print(f"${(ans):,}")



def getData():
    try:
        number = float(sys.argv[1])
        if isinstance(number, float) == False:
            raise ValueError
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        return response, float(number)
    except IndexError:
        print("Missing command-line argument ")
        sys.exit()
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()
    except requests.RequestException:
        print("There was an error fetching your results")
        sys.exit()





if __name__ == "__main__":
    main()
