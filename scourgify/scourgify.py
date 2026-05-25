import csv
import sys
#import tabulate
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

students = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last,first=row["name"].split(",")
            house=row["house"]
            students.append({"first": first.strip(),"last": last.strip(), "house": row["house"]})
            #print(f"fornavn {first} etternavn {last} hus {house}") 
except FileNotFoundError:
    sys.exit("File does not exist")


with open(sys.argv[2],'w',newline='') as ofile:
    fieldnames = ['first', 'last','house']
    writer = csv.DictWriter(ofile, fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow(student)

#for student in students:
#    print(f"fornavn {student['first']} fornavn {student['last']} og stuendten bor i {student['house']}")

