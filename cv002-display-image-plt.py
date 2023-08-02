import cv2
import matplotlib.pyplot as plt

# IMG Path
imgPath = r'mbak-ai.png'

img = cv2.imread(imgPath)
# Convert BGR to RGB (goblog bet jir)
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Using plt
plt.imshow(imgRGB)
plt.waitforbuttonpress()
plt.close('all')