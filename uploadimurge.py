import pyimgur
from draxpic import drax

def glucose_graph():
    drax()
    CLIENT_ID = "f23a5083273fb83"
    PATH = "image.png"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    return uploaded_image.link
img_url = glucose_graph()
print(img_url)