import easyocr



def findText(input):
    reader = easyocr.Reader(['hi', 'en'])
    result = reader.readtext(input,detail=0)

    return result