def main():
    print(dateChanger())

def dateChanger():
    calendar = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
    }
    while True:
        try:
            now = input("Date: ")

            #To run if the input is in month date, year format (ex. December 9, 2023)
            if "," in now:
                now = removePunc(now)

                #To split the month, date and year
                month, date, year = now.split(" ")

                #Raise a ValueError if the date is greater than 31
                if int(date) > 31:
                    raise ValueError
                print(changingStr(calendar[month], date, year))

            #To run if the input is in mm/dd/yyyy format (ex. 12/9/23)
            elif "/" in now:

                #To split the month, date and year
                m, d, y = now.split("/")

                #Raise a ValueError if the date is greater than 31 or the month is greater than 12
                if int(m) > 12 or int(d) > 31:
                    raise ValueError
                print(changingNum(m, d, y))

            #Otherwise, input is probably wrong and raise a ValueError
            else:
                raise ValueError
        except ValueError:
            continue
#Function to convert mm/dd/yyyy format to ISO 8601
def changingNum(month, date, year):
    removePunc(month)
    removePunc(date)
    date = "0" + date if int(date) < 10 else date
    month = "0" + month if int(month) < 10 else month
    return f"{year}-{month}-{date}"

#Function to convert month date, year format to ISO 8601
def changingStr(month, date, year):
    date = "0" + date if int(date) < 10 else date
    return f"{year}-{month}-{date}"

#Function to remove punctuation so the program can split accordingly
def removePunc(str):
    special = ''',.?!"':;()[]{}\\/&*%$#@+=~|^_<>`'''
    for i in special:
        str = str.replace(i, "")
    return str





main()