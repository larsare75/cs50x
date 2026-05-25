def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False

    if not s[0:2].isalpha():
        return False

    if s.find('.') != -1 or s.find(' ') != -1 or s.find(',') != -1:
        return False
    i=0
    firstnum=0
    containsnumbers=False
    while True:
        if s[i].isnumeric():
            firstnum=i
        #    print("firstnum ",firstnum)
            containsnumbers=True
            break
        else:
            i+=1
            if i>len(s)-1: break

    if s[firstnum]=="0":
        return False


    if containsnumbers==True:
        for c in s[firstnum:len(s)-1]:
            if c.isalpha():
                return False


    return True


main()
