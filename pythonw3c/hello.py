def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="World"):
    print(f"Hello, {to}!")

main()