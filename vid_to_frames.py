import cv2
import os

cam = cv2.VideoCapture("/home/danush/dataset/30-09/8.mp4")

try:

    if not os.path.exists('30-09'):
        os.makedirs('30-09')

except OSError:
    print('Error: Creating directory of data')

currentframe = 0
count = 0
while True:
    cam.set(cv2.CAP_PROP_POS_MSEC, (count * 200))
    ret, frame = cam.read()
    if ret:
        name = './30-09/8' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break
    count = count+1
cam.release()
cv2.destroyAllWindows()
