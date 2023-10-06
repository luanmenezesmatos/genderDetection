from deepface import DeepFace # Para reconhecer rostos

import cv2 # Para ler imagens

class FaceRecognition:
    # Detectar rostos
    def detectFace(self, img):
        try:
            image_path = cv2.imread(img)
            return DeepFace.extract_faces(image_path)
        except:
            return False
    
    # Reconhecer rostos
    def verifyFace(self, img1, img2):
        try:
            first_image_path = cv2.imread(img1)
            second_image_path = cv2.imread(img2)
            return DeepFace.verify(first_image_path, second_image_path)
        except:
            return False
    
    def analyzeFace(self, img):
        try:
            image_path = cv2.imread(img)

            attributesArr = ['age', 'gender', 'race', 'emotion']
            predictions = DeepFace.analyze(image_path, attributesArr)

            return predictions[0]
        except:
            return False