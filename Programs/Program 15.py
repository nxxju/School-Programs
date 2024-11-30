import cv2
img = cv2.imread('image.jpg')  # Replace with your image file path

if img is None:
    print("Error: Image not found.")
else:
    [B,G,R] = img[100, 100]
    print("Red:", R, "Green:", G, "Blue:", B)
