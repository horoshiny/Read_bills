from PIL import Image
import pytesseract,re


def all():

    # Defining paths to tesseract.exe
    # and the image we would be using
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r"C:\Users\horos\Documents\Reading bills\4.jpg"

    # Opening the image & storing it in an image object
    img = Image.open(image_path)

    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)
    a=text.replace(" ","")
    a=a.replace(",","")

    for line in a.splitlines() :
        x= re.findall(r'^TOTAL[:]*[\d]+[\.]*[\d]*|^Total[:]*[\d]+[\.]*[\d]*', line)
        price=re.findall("\d+\.*\d*", str(x))
        if price!=[]:
            df= {'Date':'2003/10/31',
                 'Prices': price[-1]}

            break
    return df
