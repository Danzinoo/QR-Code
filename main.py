import qrcode
import image
qr = qrcode.QRCode(
    version=15,  # version of the QR code, the higher the number, the bigger the code and more complicated the picture
    box_size=10,  # size of the box where qr code will be displayed
    border = 5 # White part of the image ---- border in all 4 sides with white color

)

data = "https://www.python.org/"   # link to the site --- python site
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color="white")
img.save("QRcode.png")
