# Importing library
import qrcode

# Data to encode
data = "Main to party kaar rhi thi maaze kar rhi thi"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('MyQRCode1.png')
