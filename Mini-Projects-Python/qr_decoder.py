from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C://Users//navee//Downloads//myqrcode1.png')

result = decode(img)

print(result)