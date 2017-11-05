from Crypto.Cipher import AES
import base64

#
message = "自分がしてほしいと思うことを人にもするように"
password = "920545"
iv = "L3f4m1TJtCIPV9af"
mode = AES.MODE_CBC

#
def mkpad(s, size):
    s = s.encode("utf=8")
    pad = b' ' * (size - len(s) % size)
    return s + pad

# encrypt
def encrypt(password, data):

    password = mkpad(password, 16)
    data = mkpad(data, 16)
    password = password[:16]

    aes = AES.new(password, mode, iv)
    data_cipher = aes.encrypt(data)
    return base64.b64encode(data_cipher).decode("utf-8")


def decrypt(password, encdata):

    password = mkpad(password, 16)
    password = password[:16]

    aes = AES.new(password, mode, iv)
    encdata = base64.b64decode(encdata)
    data = aes.decrypt(encdata)
    return data.decode("utf-8")


# encrypt
enc = encrypt(password, message)
# decrypt
dec = decrypt(password, enc)

# show results
print("encrypt:", enc)
print("decrypt:", dec)
