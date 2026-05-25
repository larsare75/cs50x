import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

counter = 0

try: 
    with open(sys.argv[1], "r") as file:
        for line in file:
            linje = line.lstrip()
            if not(linje.startswith("#") or linje == ""):
                counter += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(counter, end="")