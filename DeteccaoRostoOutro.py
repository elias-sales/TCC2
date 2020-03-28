from __future__ import print_function
import cv2 as cv
import os
import argparse

x = 1
def detectAndDisplay(frame):

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)# TRANSFORMA O FRAME PARA ESCALA DE CINZA
    frame_gray = cv.equalizeHist(frame_gray)#Faz a equalização de histograma para dar mais contraste à imagem


    faces = face_cascade.detectMultiScale(frame_gray)#aplica a detecção e retorna as posições no vídeo




    for (x,y,w,h) in faces:
        print(faces)
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (100, 0, 50), 4)
        faceROI = frame_gray[y:y+h,x:x+w]







    cv.imshow('Capture - Face detection', frame)#EXIBE A ELIPSE NO FRAME ATUAL



parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')

parser.add_argument('--face_cascade', help='Path to face cascade.', default='C:/Users/elias/Documents/Engenharia_Eletrica/Eye_Tracking/TCC_2/Deteccao_facial/haarcascade_frontalface_alt.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)

args = parser.parse_args()

face_cascade_name = args.face_cascade

face_cascade = cv.CascadeClassifier()

#-- 1. Carrega o modelo
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)

camera_device = args.camera

#-- 2. Lê o fluxo de vídeo
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:

    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break