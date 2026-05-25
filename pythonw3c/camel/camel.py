streng=input("camelCase: ")
print("snake_case: ",end="")
for c in streng:
    if c.isupper():
        c="_"+ c.lower()
    print(c,end="")