meny ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost=0

print(meny)
while True:
    try:
        item=input("Item: ").title()
        #if item in meny:
        total_cost+=float(meny[item])
        print(f"Total: ${total_cost:.2f}",end="")
    except KeyError:
        pass
    except EOFError:
        break