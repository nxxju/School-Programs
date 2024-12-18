# Python program to find RGB value of the image at the pixel value (100,100).

import cv2
img = cv2.imread('image.jpg')  # Replace with your image file path

if img is None:
    print("Error: Image not found.")
else:
    [B,G,R] = img[100, 100]
    print("Red:", R, "Green:", G, "Blue:", B)
