import sys
import numpy as np
from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Define the mode and key length
mode = 'png'  # or 'gif'
key_length = 16  # AES key must be either 16, 24, or 32 bytes long

# Load and convert the image
if mode == 'png':
    img = Image.open("./Lab03/tux.png").convert('RGBA')
else:
    img = Image.open("./Lab03/tux.gif").convert('P')

# Shape array (flatten & padding)
img.load()
data = np.asarray(img, dtype="uint8")
data_flat = data.flatten()
data_bytes = data_flat.tobytes()
data_padded = pad(data_bytes, AES.block_size)

# Encryption
key = get_random_bytes(key_length)
iv = get_random_bytes(AES.block_size) # only used for cbc & gcm

# choose mode of operation

# cipher = AES.new(key, AES.MODE_CBC, iv)
cipher = AES.new(key, AES.MODE_GCM, iv)
# cipher = AES.new(key, AES.MODE_ECB)

encrypted_data = cipher.encrypt(data_padded)

# discard extra bytes & reshape array (deflatten & unpadding)
encrypted_data = encrypted_data[:len(data_bytes)]
encrypted_data_flat = np.frombuffer(encrypted_data, dtype="uint8")
encrypted_data = encrypted_data_flat.reshape(data.shape)

# Case distinction (save image)
if mode == 'png':
    encrypted_img = Image.fromarray(encrypted_data, 'RGBA')
    encrypted_img.save("./Lab03/encrypted_tux.png")
else:
    encrypted_img = Image.fromarray(encrypted_data, 'P')
    encrypted_img.save("./Lab03/encrypted_tux.gif")

print("Encryption complete. Encrypted image saved.")
