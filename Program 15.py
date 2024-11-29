import cv2
img = cv2.imread('image.jpg')  # Replace with your image file path

if img is None:
    print("Error: Image not found.")
else:
    pixel_value = img[100, 100]
    print("Red:", pixel_value[2], "Green:", pixel_value[1], "Blue:", pixel_value[0])
