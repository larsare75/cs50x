import re

def main():
    email = input("What's your email? ").strip()
    checkmail(email)

def checkmail(streng):
    if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$",streng,re.IGNORECASE):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()