from src.structures.faceRecognition import FaceRecognition

import cv2

# Testar a função detectFace
img = cv2.imread('src/assets/images/rosto-feminino.jpg')
face = FaceRecognition().analyzeFace(img)