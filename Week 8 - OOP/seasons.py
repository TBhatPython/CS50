from datetime import date, datetime
import re
import inflect

class UserBirth:
    def __init__(self, date):
        self.date = datetime.strptime(date, "%Y-%m-%d")

    def __sub__(self, other):
        if isinstance(other, UserBirth):
            return self.date - other.date



def main():
    birth_date = input("Date of Birth (YYYY-MM-DD): ")
    delta_time = time_converter(birth_date)
    print(delta_time)


def time_converter(birth_date):
    matches = re.match(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", birth_date)
    if not matches:
        return "Invalid format"
    user_curr = UserBirth(str(date.today()))
    user_birth = UserBirth(birth_date)
    delta_time = (user_curr - user_birth).days * 24 * 60
    obj = inflect.engine()
    
    return f"{obj.number_to_words(int(delta_time))} minutes"

    




if __name__ == "__main__":
    main()