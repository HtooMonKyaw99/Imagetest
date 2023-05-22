from tokenize import String

from PIL.Image import Image
from django.shortcuts import render
from PIL import Image
import pytesseract
import cv2
import easyocr
# import matplotlib.pyplot as plt
from django.core.files.uploadedfile import InMemoryUploadedFile
#from pytesseract import pytesseract

#from forms import ImageUploadForm

def home(request):
    return render(request, 'home.html')


def extract_text(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        image = Image.open(image_file)
        #strs=InMemoryUploadedFile(image_file)
        #img = cv2.imread(strs)
        #reader = easyocr.Reader(['en'], gpu=False)
        #text = reader.readtext(img)
        #text=String(InMemoryUploadedFile(txt))

        # for t in text:
        #     print(t)

        texts = pytesseract.image_to_string(image)
        #text = '\n'.join([res[1] for res in texts])

        return render(request, 'extract.html', {'text': texts})
    return render(request, 'extract.html')


# from django.shortcuts import render
# import easyocr


# from django.shortcuts import render
# import easyocr
#
# def extract_text(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = request.FILES['image']
#             reader = easyocr.Reader(['en'])  # Set desired languages for OCR
#             result = reader.readtext(image)
#             extracted_text = '\n'.join([res[1] for res in result])
#             return render(request, 'result.html', {'extracted_text': extracted_text})
#     else:
#         form = ImageUploadForm()
#     return render(request, 'extract_text.html', {'form': form})

