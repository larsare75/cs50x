import csv
import sys
import tabulate
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
pizzas = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        rownum=0
        for row in reader:
            if rownum==0:
                headers = [row[0],row[1],row[2]]
            else:
                pizzas.append([row[0],row[1],row[2]])
            rownum+=1
except FileNotFoundError:
    sys.exit("File does not exist")
print(tabulate.tabulate(pizzas, headers, tablefmt="grid"))
