import qrcode

#install libs
#create function that collects link and makes a qr code
#save qrcode as png


def convert_to_qr(text):

    qr = qrcode.QRCode(version=1, 
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    imag = qr.make_image(fill_color="black", back_color="white")
    imag.save("qrimage.png")


convert_to_qr("www.google.dk")