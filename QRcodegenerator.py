import qrcode
#***To use this document you may need to install the qrcode module into python. In the terminal you can type "pip install qrcode" to install the module needed to run this program!***#
def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("QRimage001.png")

print("\nLooking To Generate a QR code for a website!\n")
url = input("Enter the url: ")
generate_qrcode(url)