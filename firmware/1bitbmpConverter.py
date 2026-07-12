#This script is not to be uploaded to the seeeduino. This is meant to convert a bmp file to a monochrome format
from PIL import Image
target = input("What .bmp to attempt to convert to 1 bit?: ")
img = Image.open(target)
img = img.convert("1")
img.save("converted.bmp")