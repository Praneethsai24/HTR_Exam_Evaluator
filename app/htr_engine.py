import pytesseract
import cv2
import numpy as np
from PIL import Image

def extract_handwritten_text(uploaded_file):
    image = Image.open(uploaded_file)
    image_array = np.array(image)

    gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)[1]

    extracted_text = pytesseract.image_to_string(processed_image, lang='eng')
    return extracted_text.strip()