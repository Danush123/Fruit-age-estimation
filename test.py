import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import datetime
import requests
from keras_preprocessing.image import img_to_array

cred = credentials.Certificate("/home/danush/Srp_Project/fir-c3697-firebase-adminsdk-gs810-3d8c01a1dc.json")

app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'fir-c3697.appspot.com',
}, name='storage')

bucket = storage.bucket(app=app)


blob = bucket.blob('images/x.jpg')

x=0
while x==0:          
    image_url=blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
    r = requests.get(image_url)
    with open("/home/danush/image.jpg", 'wb') as f:
        f.write(r.content)
    from PIL import Image   
    try:
        img = Image.open('/home/danush/image.jpg') 
        img.verify() 
    except (IOError, SyntaxError) as e:
        continue
    x=1 
    
print('Getting uploaded image...')

from keras.models import load_model
import cv2
import numpy as np 
model = load_model('/home/danush/Srp_Project/Models/Xception/my_model.h5')
image = cv2.imread('/home/danush/image.jpg')

image = cv2.resize(image, (100, 100))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)
blob = bucket.blob('upload.jpg')

(one, two, three, te, thirty) = model.predict(image)[0]
max = one
label = "one"
outfile='/home/danush/Srp_Project/Upload_images/01.jpg'
if two > max:
    max = two
    label = "two"
    outfile='/home/danush/Srp_Project/Upload_images/02.jpg'
if three > max:
    max = three
    label = "three"
    outfile='/home/danush/Srp_Project/Upload_images/03.jpg'
if te > max:
    max = te
    label = "te"
    outfile='/home/danush/Srp_Project/Upload_images/28.jpg'
if thirty > max:
    max = thirty
    label = "thirty"
    outfile='/home/danush/Srp_Project/Upload_images/30.jpg'

blob.upload_from_filename(outfile)
print(max)
print(label)

