
import numpy as np
import matplotlib.pyplot as plt
import cv2

def load_gray_image():
    img =cv2.imread('image.jpg',0)
    plt.imshow(img,'gray')
    plt.show()


