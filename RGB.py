def load_RGB_image():
    img =cv2.imread('image.jpg',1)
    plt.imshow(img,'gray')
    plt.show()


