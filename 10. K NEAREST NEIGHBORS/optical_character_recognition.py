import easyocr
from PIL import Image

# Initialize the reader
reader = easyocr.Reader(['en'])

# Path to the image file
image_path = 'example.png'

# Open the image file
img = Image.open(image_path)

# Perform OCR on the image
result = reader.readtext(image_path)

# Extract and print the text
extracted_text = ""
for detection in result:
    extracted_text += detection[1] + " "

print(extracted_text)
