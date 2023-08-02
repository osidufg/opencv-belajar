import cv2, os

imgPath = r'C:\File Fatih\VSCode\_cvPlaygrounds\mbak-ai.png'
dirPath = r'C:\File Fatih\VSCode\_cvPlaygrounds'

# Read img
img = cv2.imread(imgPath, 1)
# Change directory from workspace to intended path
os.chdir(dirPath)
# Declare filename
filename = 'savedFiles.png'
# Write file to intended path
cv2.imwrite(filename, img)
print("Successfully Saved!")
# Check directory