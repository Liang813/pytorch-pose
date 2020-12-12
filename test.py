
import cv2
import numpy as np
img = np.ones([128, 128, 3])
new_img = cv2.resize(img, (256, 128))
print(new_img.shape)
