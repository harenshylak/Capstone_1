from LSBSteg import *

#encoding
steg = LSBSteg(cv2.imread("spidey.png"))
img_encoded = steg.encode_text("Your friendly neighbourhood spiderman")
cv2.imwrite("my_new_image_1.png", img_encoded)