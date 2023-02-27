import pytesseract
from PIL import Image

# Load the image
for i in range(19,20):
    img = Image.open(f'/Users/xinchen/Desktop/{i}.jpg')
    print(f"printing {i} question")
    # Use Pytesseract to extract the text from the image
    text = pytesseract.image_to_string(img)

    # Print the text
    print(text)
