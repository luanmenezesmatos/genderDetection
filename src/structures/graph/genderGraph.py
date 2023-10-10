import pandas as pd  # Para trabalhar com dataframes
from matplotlib import pyplot as plt  # Para gerar gráficos
import os  # Para manipular arquivos

# Para configurar o layout do gráfico
from src.structures.graph.graphLayout import graphLayout
# Para baixar o gráfico localmente
from src.structures.handleUtil import handleUtil

class genderGraph:
    def __init__(self, predictions):
        self.predictions = predictions
        self.df = pd.DataFrame(self.predictions)

    def generate(self):
        # Acesse a coluna 'gender' do DataFrame
        gender_data = self.df['gender']

        # Acesse o valor associado à chave 'Woman' no dicionário
        woman_percentage = gender_data['Woman']

        # Acesse o valor associado à chave 'Man' no dicionário
        man_percentage = gender_data['Man']

        # Dados para o gráfico de pizza
        labels = ['Mulher', 'Homem']
        sizes = [woman_percentage, man_percentage]
        colors = ['pink', 'lightsteelblue']
        
        # Fazer com que o explode seja dinâmico, ou seja, explodir a fatia com maior porcentagem
        explode = []
        for i in range(len(sizes)):
            if sizes[i] == max(sizes):
                explode.append(0.1)
            else:
                explode.append(0)

        # Criar um gráfico de pizza
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=140, pctdistance=0.85, wedgeprops={'edgecolor': 'black'})
        # sizes - Valores numéricos das fatias
        # explode - Define quais fatias serão explodidas
        # labels - Rótulos das fatias
        # colors - Cores das fatias
        # autopct - Formato de exibição dos valores numéricos
        # shadow - Ativa sombra
        # startangle - Define o ângulo inicial de exibição das fatias
        # pctdistance - Define a distância dos valores numéricos em relação ao centro do gráfico
        # wedgeprops - Define as propriedades das fatias (borda)

        # Assegura que o gráfico de pizza seja um círculo.
        plt.axis('equal')

        # Define o caminho do gráfico
        graph_path = os.path.join(
            os.getcwd(), 'src', 'assets', 'graphs', 'genderGraph.png')
        # Salva o gráfico no caminho especificado (diretório local)
        plt.savefig(graph_path)

        graphLayout(plt).pie(sizes=sizes, explode=explode, labels=labels, colors=colors,
                                title='Porcentagem de Gênero')  # Configurações do gráfico de pizza

        handleUtil().saveGraph(plt) # Salva o gráfico no diretório local

        plt.show() # Exibe o gráfico