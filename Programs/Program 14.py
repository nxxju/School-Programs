import cv2
img = cv2.imread('image.png')  # Replace 'image.jpg' with the path to your image

if img is not None:
    cv2.imshow('Loaded Image', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found.")
