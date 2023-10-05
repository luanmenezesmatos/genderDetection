from deepface import DeepFace

class FaceRecognition:
    # Detectar rostos
    def detectFace(self, img):
        return DeepFace.extract_faces(img)
    
    # Reconhecer rostos
    def verifyFace(self, img1, img2):
        return DeepFace.verify(img1, img2)
    
    def analyzeFace(self, img):
        attributesArr = ['age', 'gender', 'race', 'emotion']
        predictions = DeepFace.analyze(img, attributesArr)

        return predictions[0]