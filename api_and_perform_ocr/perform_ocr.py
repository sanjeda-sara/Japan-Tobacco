import easyocr
import io
from PIL import Image
 
def perform_ocr(image_data, language='en'):
    reader = easyocr.Reader([language])
 
    try:
        # Open the image using PIL (Pillow)
        image = Image.open(io.BytesIO(image_data))
 
        # Perform OCR on the image
        result = reader.readtext(image)
 
        # Print the recognized text
        for detection in result:
            print(detection[1])
 
        return result
 
    except Exception as e:
        print(f"OCR processing failed. Error: {e}")