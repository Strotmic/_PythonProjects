#https://www.youtube.com/watch?v=XIrOM9oP3pA&t=70s

import cv2
from random import randrange

#import pre trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#import faces to look at faces and see if they show the face
#img = cv2.imread("rdj.jpg")
"""img = cv2.imread("cast.jpg")
#img = cv2.imread("bruce.jpg")

#set the pictures to greyscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#draw rectangles arround faces

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,  y ), (x + w ,y+h), (0,255,0),4 )
print(face_coordinates)

#show the picture, the waitkey makes so it doesnt close directly
cv2.imshow("Face Detector", img)
cv2.waitKey()
print("completed")

#face checking in video"""

def camera():
    webcam = cv2.VideoCapture(1)

    #loop zodat alle frames gedaan worden
    while True:

        #read the current frame
        successful_frame_read, frame = webcam.read()

        #convert to grayt scale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        #detect faces
        face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

        #draw rectangles arround faces
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x,  y ), (x + w ,y+h), (0,255,0),4 )
        print(face_coordinates)

        #als er meer dan een gezicht gescanned word zegt de python hallo
        if len(face_coordinates) >1 :
            print("hello")
        
        cv2.imshow("Face Regocnition" , frame)
        key = cv2.waitKey(1) # elke ms 

        #force stop when pressed button
        if key==50000 or key==50000:
            break

        #release the webcam
        #webcam.release()


camera()