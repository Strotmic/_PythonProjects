import cv2
from random import randrange

#import pre trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#import faces to look at faces and see if they show the face
#img = cv2.imread("rdj.jpg")
img = cv2.imread("rdj.jpg")
#img = cv2.imread("bruce.jpg")

#set the pictures to greyscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#draw rectangles arround faces

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,  y ), (x + w ,y+h), (0,50,0),4 )
print(face_coordinates)

#show the picture, the waitkey makes so it doesnt close directly
cv2.imshow("Face Detector", img)
cv2.waitKey()
print("completed")
