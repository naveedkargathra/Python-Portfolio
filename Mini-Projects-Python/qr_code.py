import qrcode

data = "Scan the QR Code:"

qr = qrcode.QRCode(version = 1, box_size=20, border =5)

qr.add_data(data)
qr.make(fit = True)



img = qr.make_image(fill_color = 'red', back_color = 'yellow')

img.save('C://Users//navee//Downloads//myqrcode1.png')

