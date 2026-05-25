def main():
    time=input("What time is it? ")
    timedec=convert(time)
    if timedec>=7 and timedec<=8:
        print("breakfast time")
    elif timedec>=12 and timedec<=13:
        print("lunch time")
    elif timedec >=18 and timedec <=19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutescalc=float(minutes)/60
    return int(hours)+minutescalc


if __name__ == "__main__":
    main()