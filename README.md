# image processing and Learning how to use Git
Specific solutions for document detection. I will describe the problems of Canny edge detection. I will also use this repository as material to learn how to use Git. I followed the instructions of https://medium.com/swlh/what-do-i-need-to-know-about-git-5017bde0b572

## Images are unique
Every gray image has a unique: 
1. Pixel intensity histogram
2. Foregroud
3. Backgroud
4. Signal to Noise ratio (SNR) which is based on foreground and background selections

## Code implementation
The code will be implemented in Python for ease of visualization. I will use some standard images and convert them into a single matrix integer baseded 8bit images. Usually to convert from RGB 3-channel based to single channel based gray scale, we take each pixel from the 3 channels and calculate there average. 


## Scripts
I added 2 scripts one that imports and plots a grayscale (gray.py) and the other as colorful (RGB.py). 
While the image processing.py runs both while importing them as packages and calling in the functions. 
