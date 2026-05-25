x,y,z=input("Expression: ").split(" ")


print(x)
print(y)
print(z)

match y:
    case "+":
        print(round(float(x)+float(z),1))
    case "-":
        print(round(float(x)-float(z),1))
    case "*":
        print(round(float(x)*float(z),1))
    case "/":
        print(round(float(x)/float(z),1))


