def load_gray_image():
    img =cv2.imread('image.jpg',0)
    plt.imshow(img,'gray')
    plt.show()


