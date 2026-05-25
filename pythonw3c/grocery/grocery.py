
liste={}

while True:
    try:
        item=input().upper()
        liste[item]=liste.get(item,0)+1
        #print(liste)
    except EOFError:
        break


listlist=sorted(liste)
#print(listlist)

for i in listlist:
    print(liste[i], i) 