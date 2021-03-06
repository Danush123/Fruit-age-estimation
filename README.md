# Fruit-age-estimation
_**An image classifier to estimate the age of fruits.**_

The image classification is done using CNN. Xception model was used for transfer learning and weights for few final layers were updated according to the training data.

The code for training and saving the model is available in [train.py](train.py) and the code for testing in [test.py](test.py)

An android application is used to select and upload the fruit's image to the Firebase storage which then triggers the execution of [test.py](test.py) code in the backend. The model then predicts the age of the fruit in the uploaded image and sends back the prediction to the firebase storage which is downloaded in the same app. The code for the app's functionality is available in [MainActivity.java](MainActivity.java)

>The project's flow:

![Flow](flow.png)

>The android application:

![Android application](app.png)

The fruit(banana) was monitored for 5 days and videos were taken each day. These videos were converted into individual images using this [code](vid_to_frames.py)
