from src.structures.handleError import handleError # Função para tratar erros

import requests # Biblioteca para fazer requisições HTTP
import os # Biblioteca para trabalhar com diretórios
import time # Biblioteca para trabalhar com tempo

class handleUtil:
    def __init__(self, img_path=None):
        self.img_path = img_path

    def verifyUrl(self):
        try:
            if requests.get(self.img_path).status_code == 200:
                return True
        except:
            return False
        
    def verifyLocalPath(self):
        if os.path.exists(self.img_path):
            return True
        
        return False

    def verifyContentTypeHeader(self):
        verifyContentTypeHeader = requests.get(self.img_path).headers['Content-Type'].split('/')[0]

        translateContentTypeHeader = {'image': 'imagem', 'video': 'vídeo', 'audio': 'áudio'}

        if not verifyContentTypeHeader == 'image':
            contentTypeTranslation = translateContentTypeHeader.get(verifyContentTypeHeader, 'página')
            handleError(f"A URL informada não é uma imagem e sim um(a) {contentTypeTranslation}", 403).sendErrorMessage()
            return False
        
        return True
    
    def downloadImage(self):
        try:
            # Verificar se na url informada possui um "?", e se tiver, remover tudo que estiver depois dele
            if '?' in self.img_path:
                self.img_path = self.img_path.split('?')[0]

            # Pegar o timestamp atual
            timestamp = str(int(time.time()))

            # Pegar a extensão da imagem
            extension = self.img_path.split('.')[-1]

            image_path = os.getcwd() + f'/src/assets/temp/temp-{timestamp}.{extension}'
            with open(image_path, 'wb') as file:
                file.write(requests.get(self.img_path).content)
            
            return image_path
        except:
            return False
        
    def saveGraph(self, plt):
        try:
            graph_path = os.path.join(os.getcwd(), 'src', 'assets', 'graphs', 'genderGraph.png') # Define o caminho do gráfico
            plt.savefig(graph_path) # Salva o gráfico no caminho especificado (diretório local)
        except:
            return False