import cv2
img = cv2.imread('image.jpg')  # Replace with your image file path

if img is None:
    print("Error: Image not found.")
else:
    pixel_value = img[100, 100]
    print("R:", pixel_value[2], "G:", pixel_value[1], "B:", pixel_value[0])
