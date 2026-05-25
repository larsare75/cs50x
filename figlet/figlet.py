import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

fonter = figlet.getFonts()
random.shuffle(fonter)

if len(sys.argv) == 1:
    #print("random")
    figlet.setFont(font=fonter[0])
elif len(sys.argv) ==3:
    #print("format oppgitt") 
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    if sys.argv[2] not in fonter:
        sys.exit("Invalid usage")
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

tekst=input("Input: ")

print(figlet.renderText(tekst))