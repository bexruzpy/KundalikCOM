import re
import cv2
import numpy as np
from pytesseract import pytesseract, image_to_string
pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract.exe'  # Tesseract-OCR ning joylashuvi

# Rasmingizni yuklash
def to_str(file) -> str:
    nparr = np.frombuffer(file, np.uint8)
    # Decode the image from the NumPy array
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    lower = np.array([0, 0, 0], dtype=np.uint8)
    upper = np.array([50, 50, 50], dtype=np.uint8)

    # Rasmni BGR dan HSV ga o'girish
    image = cv2.threshold(image, 190, 250, cv2.THRESH_BINARY)[1]
    # cv2.imshow("awdwd",image)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # O'q ranglarni tanlash
    mask = cv2.inRange(hsv_image, lower, upper)

    # Oq ranglar ustida konturlarni aniqlash
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Har bir konturni aylantirish
    for contour in contours:
        # Konturlarni kvadratga aylantirish
        x, y, w, h = cv2.boundingRect(contour)
        if w < 3 and h < 3:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), -1)
        # Matnni aniqlash
    text = image_to_string(image, config='--psm 6 outputbase digits')

    # Aniqlangan matnni qaytarish
    return re.sub(r'\D', '', text)
# print(to_str("C:\\Users\\Bexruz vlog\\Downloads\\b643c9f5-316a-4ea0-b801-4a35a41a3a19.jpg"))
# print(pytesseract.image_to_string("C:\\Users\\Bexruz vlog\\Downloads\\b643c9f5-316a-4ea0-b801-4a35a41a3a19.jpg", config='--psm 6 outputbase digits'))













