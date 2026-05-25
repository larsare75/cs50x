import re

def main():
    name = input("What's your name? ").strip()
    print(cleaninput(name))


def cleaninput(name):
    matches = re.search(r"^(.+), *(.+)$",name)
    if matches:
        name = matches.group(2) + " " + matches.group(1)
    return(f"hello, {name}")



if __name__ == "__main__":
    main()