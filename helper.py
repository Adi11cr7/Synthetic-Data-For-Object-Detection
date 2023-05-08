# Standard imports
import cv2
import numpy as np;
import os
import time
import random
import sys

colors = ([1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [0, 1, 1], [1, 0, 1])
input_folder = sys.argv[1]
output_folder = sys.argv[2]
try:
    os.mkdir(os.path.join(os.path.join(output_folder, "imgs")))
    os.mkdir(os.path.join(os.path.join(output_folder, "masks")))
except Exception:
    pass

for file in os.listdir(input_folder):
    print(file)
    img = cv2.imread(os.path.join(input_folder,file))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 10,255, cv2.THRESH_BINARY_INV)
    
    #coloring
    RGB = random.randint(0, len(colors)-1)  
    # img[thresh == 0] *= np.array(colors[RGB], dtype='uint8')
    
    cv2.waitKey(0)
    
    #writing to files
    print(cv2.imwrite(os.path.join(os.path.join(output_folder, "imgs", file)), img))
    cv2.imwrite(os.path.join(os.path.join(output_folder, "masks", file)), thresh)
    print(os.path.join(os.path.join(output_folder, "masks", file)), thresh)
    # cv2.imshow('Image', img)
    # cv2.imshow("mask",thresh)
    # cv2.waitKey(0)
cv2.destroyAllWindows()