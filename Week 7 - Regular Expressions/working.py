import re

def main():
    print(convert(input("Hours: ")))


def convert(hours):
    matches = re.search(r"^([0-9]+)(?::([0-9]+))? (AM|PM) to ([0-9]+)(?::([0-9]+))? (AM|PM)$", hours)

    if not matches:
         return "Invalid time"
    
    try:
        start_hour, start_minute, start_meridian, end_hour, end_minute, end_meridian = matches.groups()
        start_hour, end_hour = int(start_hour), int(end_hour)
        start_minute = int(start_minute or "0")
        end_minute = int(end_minute or "0")

        start_hour = start_hour + 12 if start_meridian == "PM" and start_hour != 12 else start_hour
        start_hour = 0 if start_meridian == "AM" and start_hour == 12 else start_hour
        end_hour = end_hour + 12 if end_meridian == 'PM' and end_hour != 12 else end_hour
        end_hour = 0 if end_meridian == "AM" and end_hour == 12 else end_hour
        
        if (start_hour > 23) or (end_hour > 23) or (start_minute > 59) or (end_minute > 59):
            raise ValueError
        return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"
    except ValueError:
         return "Invalid time"
    

if __name__ == "__main__":
    main()