while True:
    fraction=input("Fraction: ")
    tall=fraction.split("/")
    try:
        percentage=round((int(tall[0])/int(tall[1]))*100)
    except (ZeroDivisionError,ValueError):
        pass
    else:
        if percentage>100 or percentage<0:
            pass
        else:
            break

if percentage<=1:
    print("E")
elif percentage>=99:
    print("F")
else:
    #print(f"{percentage}%")
    print(str(percentage)+"%",end="")
