import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=1)


# qr.add_data(UNICODE_TEXT)
qr.add_data("https://www.youtube.com/")

qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")

img.save("youtube.png")