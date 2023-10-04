from deepface import DeepFace

class FaceRecognition:
    # Detectar rostos
    def detectFace(self, img):
        return DeepFace.extract_faces(img)
    
    # Reconhecer rostos
    def verify(self, img1, img2):
        return DeepFace.verify(img1, img2)