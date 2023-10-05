from src.structures.faceRecognition import FaceRecognition

import cv2
import os

# Testar a função detectFace
image_path = os.getcwd() + '/src/assets/images/rosto-feminino.jpg'
img = cv2.imread(image_path)
face = FaceRecognition().analyzeFace(img)

data = face['age']
print(data)