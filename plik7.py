from PIL import Image
import pytesseract
pytesseract.image_to_string(Image.open('images/photo-text.jpg'))