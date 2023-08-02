import cv2

# IMG Path
imgPath = r'assets\windah-bocil.jpg'
imgName = r'BOCHIL'

# Read image
# Flags: 1 (RGB), 0 (Grayscale), -1 (RGBA)
img = cv2.imread(imgPath, -1)

# Display image in GUI
cv2.imshow(imgName, img)

# Wait window until user closes, then remove from memory
cv2.waitKey(0)
cv2.destroyAllWindows()

