import qrcode
import PIL

qr = qrcode.QRCode()
qr.add_data('https://github.com/pythauresk/projet-livre')  # meta
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("test.png")


if __name__ == "__main__":
    pass
