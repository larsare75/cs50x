import random

def main():
    n=get_posint("Level: ")
    rand=random.randint(1,n)
    print(f"tilfeldig {rand}")
    while True:
        guess=get_posint("Guess: ")
        if guess < rand:
            print("Too small!")
        elif guess > rand:
            print("Too large!")
        else:
            print("Just right!")
            break        

def get_posint(prompt):
    while True:
        try:
            x= int(input(prompt))
        except ValueError:
            pass
        else:
            if x<1:
                pass
            else:
                return x

main()

