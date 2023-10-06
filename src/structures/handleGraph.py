import pandas as pd
from matplotlib import pyplot as plt

class HandleGraph:
    def __init__(self, predictions):
        self.predictions = predictions

    def dataProcessing(self):
        # Criar um dataframe
        df = pd.DataFrame(self.predictions)

        print(df)

        """ # Transformar em tabela
        data = data.T

        # Renomear colunas
        data.columns = ['Predicted', 'Real']

        # Transformar em inteiro
        data = data.astype(int)

        # Transformar em string
        data = data.astype(str)

        # Substituir valores
        data = data.replace('0', 'Normal')

        # Substituir valores
        data = data.replace('1', 'Fraude')

        # Transformar em inteiro
        data = data.astype(str) """