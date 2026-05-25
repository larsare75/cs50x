
import os
import csv
import sys
#import tabulate

from PIL import Image
from PIL import ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

before=sys.argv[1].lower()
after=sys.argv[2].lower()


if  not before.endswith((".jpg",".jpeg",".png")):
    sys.exit("Invalid input")

if  not after.endswith((".jpg",".jpeg",".png")):
    sys.exit("Invalid input")

if os.path.splitext(before)[1] != os.path.splitext(after)[1]:
    sys.exit("Input and output have different extensions")

shirt=Image.open("shirt.png")

photo=Image.open(sys.argv[1])
size=shirt.size

adjustedimage=ImageOps.fit(photo,size)

adjustedimage.paste(shirt,shirt)

adjustedimage.save(
    sys.argv[2]
)