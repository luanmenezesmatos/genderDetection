import pandas as pd # Para trabalhar com dataframes
import numpy as np # Para trabalhar com arrays
from matplotlib import pyplot as plt # Para gerar gráficos
import os # Para manipular arquivos
import random # Para gerar cores aleatórias

# Para configurar o layout do gráfico
from src.structures.graph.graphLayout import graphLayout
# Para baixar o gráfico localmente
from src.structures.handleUtil import handleUtil


class raceGraph:
    def __init__(self, predictions):
        self.predictions = predictions
        self.df = pd.DataFrame(self.predictions)

    def generate(self):
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

        # Fazer com que o explode seja dinâmico, ou seja, explodir a fatia com maior porcentagem
        explode = []
        for i in range(len(sizes)):
            if sizes[i] == max(sizes):
                explode.append(0.1)
            else:
                explode.append(0)

        # Adicionar labels apenas nas fatias com porcentagem maior que 5%
        labels = [labels[i] if sizes[i] >= 5 else '' for i in range(len(sizes))]

        # Adicionar colors de acordo com a quantidade de fatias presentes em labels
        colors = [colors[i] for i in range(len(labels)) if labels[i] != ''] # Se o label for vazio, não adicionar a cor

        # Criar um gráfico de pizza
        # Criar uma nova lista de tamanhos que contém apenas os tamanhos das fatias que atendem ao critério
        filtered_sizes = [size if size >= 5 else 0 for size in sizes]
        plt.pie(filtered_sizes, labels=labels, explode=explode, colors=colors,
            shadow=True, startangle=140, pctdistance=0.85, wedgeprops={'edgecolor': 'black'})
        
        # Inserir legenda no gráfico (apenas nas fatias com porcentagem maior que 5%) e retirar as cores da legenda
        # plt.legend(labels, title='Raça', loc='best', facecolor='white', edgecolor='black')

        """ plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90) """

        # plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.2f%%')

        # Define o caminho do gráfico
        graph_path = os.path.join(
            os.getcwd(), 'src', 'assets', 'graphs', 'raceGraph.png')
        # Salva o gráfico no caminho especificado (diretório local)
        plt.savefig(graph_path)

        """ graphLayout(plt).pie(type='race', sizes=sizes, explode=explode, labels=labels, colors=colors,
                     title='Porcentagem de Raça')  # Configurações do gráfico de pizza """

        handleUtil().saveGraph(plt)

        plt.show()  # Exibe o gráfico
