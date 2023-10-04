from src.structures.faceRecognition import FaceRecognition

import cv2
import os

# Testar a função detectFace
img = cv2.imread('src/assets/images/rosto-feminino.jpg')
face = FaceRecognition().detectFace(img)
print(face)