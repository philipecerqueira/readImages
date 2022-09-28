import cv2
import pytesseract

image = cv2.imread("01.jpeg")
imageRgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(imageRgb, lang='por')

print(text)
