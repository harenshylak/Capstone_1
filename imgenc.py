from pil import Image
from rubikencryptor import RubikCubeCrypto

# Encrypt image
input_image = Image.open('my_new_image_1.png')
encryptor = RubikCubeCrypto(input_image)
encrypted_image = encryptor.encrypt(alpha=8, iter_max=10, key_filename='key.txt')
encrypted_image.save('encrypted_image.png')