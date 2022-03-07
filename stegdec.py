from LSBSteg import *

#decoding
im = cv2.imread("decrypted_image.png")
steg = LSBSteg(im)
print("Text value:",steg.decode_text())