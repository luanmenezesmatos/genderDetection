from src.structures.faceRecognition import FaceRecognition # Função para reconhecer faces
from src.structures.selectOption import selectOption # Função para selecionar uma opção
from src.structures.handleError import handleError # Função para tratar erros
from src.structures.handleUtil import handleUtil # Função para tratar utilidades
from src.structures.handleGraph import HandleGraph # Função para tratar gráficos

import os # Biblioteca para trabalhar com diretórios

select = selectOption("Como você deseja analisar a imagem?", ["Analisar uma imagem pelo arquivo do diretório local", "Analisar uma imagem pela URL"]).choose()

match select:
    case 1:
        image_path = input("Digite o caminho da imagem: ")

        # Verificar se o arquivo existe no diretório local
        if not handleUtil(image_path).verifyLocalPath():
            handleError("O arquivo não é uma imagem", 400).sendErrorMessage()
            exit()

        face = FaceRecognition().analyzeFace(image_path)

        print(face)
    case 2:
        image_url = input("Digite a URL da imagem: ")

        # Verificar se a URL informada existe usando o requests.get()
        if not handleUtil(image_url).verifyUrl():
            handleError("A URL informada não existe!", 404).sendErrorMessage()
            exit()

        # Verificar se a URL informada é uma imagem usando o requests.get()
        if not handleUtil(image_url).verifyContentTypeHeader():
            exit()

        # Verificar se a URL informada não é um arquivo do diretório local
        if handleUtil(image_url).verifyLocalPath():
            handleError("Nós só permitimos imagens que estejam em um servidor!", 403).sendErrorMessage()
            exit()

        # Função para acessar a imagem usando o requests.get() e baixar localmente em uma pasta temporária
        downloaded_image = handleUtil(image_url).downloadImage()

        if not downloaded_image:
            handleError("Ocorreu um erro ao baixar a imagem! Tente novamente.", 500).sendErrorMessage()
            exit()

        if os.path.exists(downloaded_image):
            detectFace = FaceRecognition().detectFace(downloaded_image)
            if detectFace:
                analyzeFace = FaceRecognition().analyzeFace(downloaded_image)

                os.remove(downloaded_image)

                HandleGraph(analyzeFace).dataProcessing()
            else:
                handleError("Não foi possível detectar nenhum rosto na imagem!", 400).sendErrorMessage()
                os.remove(downloaded_image)
                exit()

            """ face = FaceRecognition().analyzeFace(downloaded_image)
            os.remove(downloaded_image)

            print(face) """
        else:
            handleError("Ocorreu um erro ao baixar a imagem!", 500).sendErrorMessage()
            exit()

        # Analisar a imagem usando o DeepFace.analyze()
        # face = FaceRecognition().analyzeFace(requests.get(image_url, stream=True).raw)

        #print(face)
    case _:
        handleError("Opção inválida! Tente novamente.", 400).sendErrorMessage()
        exit()

""" # Testar a função detectFace
image_path = os.getcwd() + '/src/assets/images/rosto-feminino.jpg'
face = FaceRecognition().analyzeFace(image_path)

# data = face['age']

print(face) """