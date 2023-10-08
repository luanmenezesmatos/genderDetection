from src.structures.faceRecognition import FaceRecognition # Função para reconhecer faces
from src.structures.selectOption import selectOption # Função para selecionar uma opção
from src.structures.handleError import handleError # Função para tratar erros
from src.structures.handleUtil import handleUtil # Função para tratar utilidades
from src.structures.handleGraph import HandleGraph # Função para tratar gráficos

from config import appConfig # Configurações do app

import os # Biblioteca para trabalhar com diretórios
import json # Biblioteca para trabalhar com JSON

select = selectOption("Como você deseja analisar a imagem?", ["Analisar uma imagem pelo arquivo do diretório local", "Analisar uma imagem pela URL"]).choose()

match select:
    case 1:
        # Criar uma expressão ternária, verificando se usará o diretório local do computador do desenvolvedor ou do Senac
        computer_image_path = os.getenv('MY_OWN_COMPUTER_IMAGE_PATH') if appConfig().is_my_computer else os.getenv('SENAC_COMPUTER_IMAGE_PATH')
        
        if appConfig().is_development:
            print("Entrou em fase de desenvolvimento")

            image_path = computer_image_path

            # Verificar se o arquivo existe no diretório local
            if not handleUtil(image_path).verifyLocalPath():
                handleError("O arquivo não é uma imagem", 400).sendErrorMessage()
                exit()
            
            # Ler um arquivo de exemplo em JSON para testar as funções de análise de imagem e geração de gráficos
            with open(os.getcwd() + '/predictions.json', 'r') as file:
                data = json.load(file)

            HandleGraph(predictions=data, app_environment='development').dataProcessing()
        elif appConfig().is_production:
            print("Entrou em fase de produção")

            image_path = input("Digite o caminho da imagem: ")

            # Verificar se o arquivo existe no diretório local
            if not handleUtil(image_path).verifyLocalPath():
                handleError("O arquivo não é uma imagem", 400).sendErrorMessage()
                exit()

            face = FaceRecognition().analyzeFace(image_path)

            HandleGraph(predictions=face, app_environment='production').dataProcessing()
        else:
            print("O modo escolhido no arquivo de configuração (.env) não é válido!")
            exit()
    case 2:
        # Criar uma expressão ternária, verificando no appConfig() se o modo escolhido é 'development' ou 'production', e se for 'development', usar uma URL de exemplo, caso contrário, usar a URL informada pelo usuário
        image_url = os.getenv('EXAMPLE_IMAGE_URL') if appConfig().is_development else input("Digite a URL da imagem: ")

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
                print("Rosto detectado!")

                config = appConfig()

                if config.is_production:
                    print("Entrou em fase de produção")

                    analyzeFace = FaceRecognition().analyzeFace(downloaded_image)

                    os.remove(downloaded_image)

                    HandleGraph(predictions=analyzeFace, app_environment='production').dataProcessing()
                elif config.is_development:
                    print("Entrou em fase de desenvolvimento")

                    os.remove(downloaded_image)
                    
                    # Ler um arquivo de exemplo em JSON para testar as funções de análise de imagem e geração de gráficos
                    with open(os.getcwd() + '/predictions.json', 'r') as file:
                        data = json.load(file)

                    HandleGraph(predictions=data, app_environment='development').dataProcessing()
                else:
                    os.remove(downloaded_image)

                    print("O modo escolhido no arquivo de configuração (.env) não é válido!")
                    exit()
            else:
                handleError("Não foi possível detectar nenhum rosto na imagem!", 400).sendErrorMessage()
                os.remove(downloaded_image)
                exit()
        else:
            handleError("Ocorreu um erro ao baixar a imagem!", 500).sendErrorMessage()
            exit()
    case _:
        handleError("Opção inválida! Tente novamente.", 400).sendErrorMessage()
        exit()