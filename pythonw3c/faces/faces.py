def convert(streng):
    return streng.replace(":)", "🙂").replace(":(", "🙁")

def main():
    print(convert(input("Skriv inn en streng med smilefjes: ")))

main()