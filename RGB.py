import numpy as np
import matplotlib.pyplot as plt
import cv2

def load_RGB_image():
    img =cv2.imread('image.jpg',1)
    plt.imshow(img)
    plt.show()


