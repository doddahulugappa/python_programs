import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://github.com/doddahulugappa/')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white", image_factory=StyledPilImage)
img.save("qrcode.png")