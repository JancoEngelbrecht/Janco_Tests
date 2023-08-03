import qrcode


data = "Name of Product"

# WHITE QR CODE
img = qrcode.make(data)
img.save("D:/4. Python Programs/Y2023/1. Mad libs Python Project/myqrcode.png")

# RED QR CODE
qr = qrcode.QRCode(version=1, box_size=10, border=5)  # Technical Specs from the imported library
qr.add_data(data)
qr.make(fit=True)  # Technical Specs from the imported library
img = qr.make_image(back_color='Black', fill_color='Green')  # Technical Specs from the imported library
img.save('D:/4. Python Programs/Y2023/1. Mad libs Python Project/myqrcode1.png')
