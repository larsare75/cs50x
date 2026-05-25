import inflect

p=inflect.engine()

lines = []

while True

    try:
        line=input("Name: ")
        lines.append(line)
    except EOFError:
        break

print("Adieu, adieu, to "+p.join(lines, final_sep=""))
