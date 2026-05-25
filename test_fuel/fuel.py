
def main():
    fraction=input("Fraction: ")
    print(gauge(convert(fraction)))

def convert(fraction):
    tall=fraction.split("/")
    if int(tall[0])<0 or int(tall[1])<0:
        raise ValueError
    return round((int(tall[0])/int(tall[1]))*100)


def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    return f"{percentage}%"

if __name__ == "__main__":
    main()