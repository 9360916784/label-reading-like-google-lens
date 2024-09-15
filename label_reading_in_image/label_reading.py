try:
    from PIL import Image
except ImportError:
    import Image
    
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

info = recText('TEST4.jpg')
print(info)

with open("New.txt", "a") as file:
    file.write(info)

print("Written Successfully")
