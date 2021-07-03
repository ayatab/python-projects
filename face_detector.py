import cv2
# print("hey world")

# we will be using haarcascade in opencv for facial recognition
#Cascade allows you to classify things, in this case the face data
face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

