import re
import sys
def main():
    print(convert(input("Hours: ")))
def convert(s):
    matches=re.search(r'([0-1]?[0-9]):?([0-5][0-9])? (AM|PM) to ([0-1]?[0-9]):?([0-5][0-9])? (AM|PM)',s)
    if matches:
        starthour=int(matches.group(1))
        if matches.group(2)== None:
            startmin="00"
        else:
            startmin=matches.group(2)
        endhour=int(matches.group(4))
        if matches.group(5) == None:
            endmin="00"
        else:
            endmin=matches.group(5)
        if matches.group(3)=="PM" and starthour!=12:
            starthour+=12
        if matches.group(6)=="PM" and endhour!=12:
            endhour+=12

        if starthour==12 and matches.group(3)=="AM":
            starthour="00"

        if endhour==12 and matches.group(5)=="AM":
            endhour="00"

        return (f"{starthour:02}:{startmin:02} to {endhour:02}:{endmin:02}")
    else:
        raise ValueError()





if __name__ == "__main__":
    main()
