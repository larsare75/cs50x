maaneder=    [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

datostreng=input("Date: ")
try:
    dato=datostreng.split("/")
    if len(dato)==3:
        dag=int(dato[0])
        maaned=int(dato[1])
        aar=int(dato[2])
    else:
        dato=datostreng.split(" ")
        dag=int(dato[1][:-1])
        maaned=maaneder.index(dato[0])+1
        aar=int(dato[2])    
except (ValueError,IndexError):
    print("Invalid date")
else:    print(f"{aar:04d}-{maaned:02d}-{dag:02d}")


