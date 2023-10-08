import os

from dotenv import load_dotenv
load_dotenv()

class appConfig:
    # Função para escolher entre os modos de 'development' ou 'production' - deverá ser setada por padrão para 'development' através de uma variável de ambiente
    def __init__(self):
        self.APP_ENV = os.getenv('APP_ENV')
        self.IMAGE_COMPUTER_ENV = os.getenv('IMAGE_COMPUTER_ENV')

        self.is_development = False # Se for 'True', o programa irá rodar em modo de desenvolvimento, caso contrário, irá rodar em modo de produção
        self.is_production = False # Se for 'True', o programa irá rodar em modo de produção, caso contrário, irá rodar em modo de desenvolvimento

        self.is_my_computer = False # Se for 'True', o programa irá rodar no próprio computador do desenvolvedor
        self.is_senac_computer = False # Se for 'True', o programa irá rodar no computador do Senac

        self.verifyEnv() # Chamando a função no construtor
    
    # Função para fazer a verificação do valor da variável de ambiente 'APP_ENV'
    def verifyEnv(self):
        # Verificar se a variável de ambiente 'APP_ENV' é igual a 'development' ou 'production'
        if self.APP_ENV == 'development':
            self.is_development = True
        elif self.APP_ENV == 'production':
            self.is_production = True
        else:
            # Deixe o bloco else vazio
            pass

        # Verificar se a variável de ambiente 'IMAGE_COMPUTER_ENV' é igual a 'my_computer' ou 'senac_computer'
        if self.IMAGE_COMPUTER_ENV == 'my_computer':
            self.is_my_computer = True
        elif self.IMAGE_COMPUTER_ENV == 'senac_computer':
            self.is_senac_computer = True
        else:
            # Deixe o bloco else vazio
            pass