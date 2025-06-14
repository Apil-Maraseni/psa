import pyqrcode

text = input("Enter the text to generate QR code:")

qr_code = pyqrcode.create(text)     # object of pyqrcode create() with text as an argument

qr_code.svg("qr_code.svg", scale =8)   #svg() format of qr code