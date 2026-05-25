amount_due=50

while amount_due > 0:
    print("Amount Due: "+ str(amount_due))
    coin=input("Insert Coin: ")
    if int(coin) in(25,10,5):
        amount_due-=int(coin)

print("Change Owed:",abs(amount_due))