import inflect

p=inflect.engine()

lines = []

while True:

    try:
        line=input("Name: ")
        lines.append(line)
    except EOFError:
        print()
        break
print("Adieu, adieu, to "+p.join(lines))
