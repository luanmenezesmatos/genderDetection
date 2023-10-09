import pandas as pd  # Para trabalhar com dataframes
import numpy as np  # Para trabalhar com arrays
from matplotlib import pyplot as plt  # Para gerar gráficos
import os  # Para manipular arquivos

# Para configurar o layout do gráfico
from src.structures.graph.graphLayout import graphLayout
# Para baixar o gráfico localmente
from src.structures.handleUtil import handleUtil


class raceGraph:
    def __init__(self, predictions):
        self.predictions = predictions
        self.df = pd.DataFrame(self.predictions)

    def generate(self):
        print(self.df)

        # Acesse a coluna 'race' do DataFrame
        race_data = self.df['race']

        # Acesse os valores associados às chaves no dicionário
        asian_percentage = race_data['asian']
        indian_percentage = race_data['indian']
        black_percentage = race_data['black']
        white_percentage = race_data['white']
        middle_eastern_percentage = race_data['middle eastern']
        latino_hispanic_percentage = race_data['latino hispanic']

        # Dados para o gráfico de pizza
        labels = ['Asiático', 'Indiano', 'Preto',
                  'Branco', 'Oriente Médio', 'Latino']
        sizes = [asian_percentage, indian_percentage, black_percentage,
                 white_percentage, middle_eastern_percentage, latino_hispanic_percentage]
        colors = ['lightcoral', 'darkorange', 'black',
                  'white', 'yellowgreen', 'lightblue']
        # explode = (0, 0, 0, 0, 0, 0) # Não explode nenhuma fatia

        # Fazer com que o explode seja dinâmico, ou seja, explodir a fatia com maior porcentagem
        explode = []
        for i in range(len(sizes)):
            if sizes[i] == max(sizes):
                explode.append(0.1)
            else:
                explode.append(0)

        print(explode)

        # Criar um gráfico de pizza
        """ plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=140, pctdistance=0.85, wedgeprops={'edgecolor': 'black'}) """

        """ plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90) """

        plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.2f%%')

        # Define o caminho do gráfico
        graph_path = os.path.join(
            os.getcwd(), 'src', 'assets', 'graphs', 'raceGraph.png')
        # Salva o gráfico no caminho especificado (diretório local)
        plt.savefig(graph_path)

        """ graphLayout(plt).pie(type='race', sizes=sizes, explode=explode, labels=labels, colors=colors,
                             title='Porcentagem de Raça')  # Configurações do gráfico de pizza """

        handleUtil().saveGraph(plt)

        plt.show()  # Exibe o gráfico
