# import package
import qrcode
# generate QR code
img = qrcode.make("http://fukuzawalab.com/")
# save to file
img.save("qrcode-test.png")
