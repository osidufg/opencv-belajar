import cv2, matplotlib.pyplot as plt

# Deklarasi image path
imagePath = r'assets\windah-bocil.jpg'

# Read Image
img = cv2.imread(imagePath)

# Grayscale better for detection
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Load classifier
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
# Detect face
face = face_classifier.detectMultiScale(
    img_gray, scaleFactor = 1.1, minNeighbors = 10, minSize = (40,40)
)
# Drawing box
# cv2.rectangle = bikin kotak
# x, y, w, h = posisi muka dan panjang-lebar nya
# 0, 255, 0 = warna hijau
# 4 = ketebalan
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w , y + h), (0, 255, 0), 4)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb) 
plt.axis('off')
plt.waitforbuttonpress()
plt.close('all')


