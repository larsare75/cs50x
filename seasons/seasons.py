import datetime
import sys
import re
import inflect

def get_birthdate():
    return input("Date of Birth:")

def check_birthdate(dato):
    if re.fullmatch(r'([0-9]{4})-(0[1-9]|1[0-2])-([0][1-9]|[1-2][0-9]|[3][0-1])',dato):
        return True
    else:
        return False

def main():
    birthdate=get_birthdate()
    if not check_birthdate(birthdate):
        sys.exit(1)
    bdate=datetime.date.fromisoformat(birthdate)
    deltatime=datetime.date.today()-bdate
    minutes=deltatime.days*24*60
    p = inflect.engine()
    print(p.number_to_words(minutes, andword="").capitalize(), 'minutes')

if __name__ == "__main__":
    main()
