name=input("Hva heter du: ")

filen=open("navfil.txt","a")
filen.write(f"{name}\n")
filen.close()