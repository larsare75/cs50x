import re

def extract(url: str)->str:
    username = re.sub(r"^(https?://)(www\.)?twitter\.com/","",url)
    return username

def main():
    url = input("URL: ").strip()
    print(extract(url))

if __name__ == "__main__":
    main()