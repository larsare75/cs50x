def main():
    rettetstreng=shorten(input("Input: "))
    print(f"Output: {rettetstreng}")

def shorten(word):
    streng=""
    for c in word:
        #print(f"runde {c}")
        #print(f"runde {c.upper()}")
        if c.upper() not in('A','E', 'I', 'O', 'U'):
            #print("jeg er her")
            #print(c,end="")
            streng=streng+c;
    return streng

if __name__ == "__main__":
    main()
