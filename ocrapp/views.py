from tokenize import String

from django.shortcuts import render
import easyocr


def extract_text(image):
    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])

    # Perform OCR on the image
    result = reader.readtext(image)

    # Extract the text line by line
    lines = [line[1] for line in result]

    return lines


def home(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Get the uploaded image file
        image = request.FILES['image']

        # Extract the text from the image
        lines = extract_text(image)

        # Pass the lines of text to the template
        return render(request, 'result.html', {'lines': lines})

    return render(request, 'home.html')
