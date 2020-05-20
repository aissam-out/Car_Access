import re
import cv2
import pytesseract
from PIL import Image

#image_path = "cin1.jpeg"

def crop(image_path, saved_location):
    #w= 1027 h=652
    image_obj = Image.open(image_path)
    w, h = image_obj.size
    coords = 0.68*w, 0.7*h, 0.88*w, 0.88*h

    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    #cropped_image.show()
    #print("height ",h)
    #print("width ", w)

    return cropped_image

#crop(image_path, 'cropped.jpg')
def togrey(image, saved_location):
    img = Image.open(image).convert('LA')
    img.save(saved_location)

    return img

def extact_text(image):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = cv2.imread(image)
    text = pytesseract.image_to_string(img)
    text = re.sub('[^A-Z0-9]+', '', text)
    print(text)
    return text
