import fitz  # PyMuPDF
from PIL import Image
import cv2
import numpy as np
from pytesseract import image_to_string

def extract_last_page(pdf_path):
    pdf_document = fitz.open(pdf_path)
    last_page = pdf_document[-1]  # Get the last page
    pix = last_page.get_pixmap()  # Get page image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img

def analyze_color(img):
    img_cv = np.array(img)
    img_hsv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2HSV)
    
    # Analyze dominant color, specific hue ranges, etc.
    # For example, detecting if the page is mostly a certain color
    dominant_color = np.mean(img_hsv, axis=(0, 1))
    
    return dominant_color

def detect_blue_pen(img):
    img_cv = np.array(img)
    img_hsv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2HSV)
    
    # Define range for blue color in HSV
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    
    # Threshold the image to find blue areas
    mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
    blue_detected = np.sum(mask) > 0  # Check if any blue is detected
    
    return blue_detected

def check_back_cover(pdf_path):
    img = extract_last_page(pdf_path)
    dominant_color = analyze_color(img)
    blue_pen = detect_blue_pen(img)
    
    #if not blue_pen and dominant_color.any():  # Assuming dominant_color check will involve more logic

    if blue_pen:
        if (dominant_color[0] > 80):
            return "Likely Back Cover"
    else:
        return "Normal Page"

pdf_path = "ALHC00015130.pdf"
result = check_back_cover(pdf_path)
print(result)
