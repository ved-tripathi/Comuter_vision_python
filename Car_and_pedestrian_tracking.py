import cv2 as cv

#feeding the image
# img_file = 'Car_image.jpeg'
video = cv.VideoCapture('Tesla Autopilot Dashcam Complication 2021 Version.mp4')

#Trained car Classifier
car_classifier = 'car_detector.xml'

#Run forever until car stops 
while True:
    read_successful, frame = video.read() 

    #safe coding
    if read_successful:
        #convwersion to gray scale
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    else:
        break

    #Display the image with the faces spotted
    cv.imshow('vid', gray_frame)
    print('program chal raha hai')
    #Don't autoclose
    cv.waitKey(1)

'''
#callling the image in opencv
img = cv.imread(img_file)

#converting to gray scale because the machine acceptss olny grasyscale images
gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#calling the car classifier machine
car_tracker = cv.CascadeClassifier(car_classifier)

#imposing the image in thwe machine
cars = car_tracker.detectMultiScale(gray_scale)
print(cars)

# Draw rectangle after detecting
for x,y,w,h in cars:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
    cv.putText(img, "car", (x+w, y+w), cv.FONT_HERSHEY_DUPLEX, 1.0, (0,0,255), 1)

#Displaying the call
cv.imshow('main', img)

# adding a delay to the output
cv.waitKey()'''