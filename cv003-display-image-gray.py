import cv2

# IMG Path
imgPath = r'mbak-ai.png'
imgName = r'si mbak cangtip'

img = cv2.imread(imgPath, 0)
# Image shape attribute
print(img.shape)

cv2.imshow(imgName, img)
cv2.waitKey(0)
cv2.destroyAllWindows()