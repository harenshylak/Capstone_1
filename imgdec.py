from pil import Image
from rubikencryptor import RubikCubeCrypto

# Decrypt image
encrypted_image = Image.open('encrypted_image.png')
decryptor = RubikCubeCrypto(encrypted_image)
decrypted_image = decryptor.decrypt(key_filename='key.txt')
decrypted_image.save('decrypted_image.png')