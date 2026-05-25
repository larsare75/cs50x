streng=input("Input: ")
print("Output: ")
for c in streng:
    if c.upper() not in('A','E', 'I', 'O', 'U'):
        print(c,end="")