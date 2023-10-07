import pandas as pd # Para trabalhar com dataframes
from matplotlib import pyplot as plt # Para gerar gráficos
import os # Para manipular arquivos

from src.structures.graph.graphLayout import graphLayout # Para configurar o layout do gráfico

class genderGraph:
    def __init__(self, predictions):
        self.predictions = predictions
        self.df = pd.DataFrame(self.predictions)

    def generate(self):
        try:
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
            explode = (0.1, 0)  # Explodir a primeira fatia (Mulher)

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

            plt.axis('equal') # Assegura que o gráfico de pizza seja um círculo.

            # plt.tight_layout() # Ajusta o layout do gráfico

            # plt.title('Porcentagem de Gênero') # Define o título do gráfico

            graph_path = os.path.join(os.getcwd(), 'src', 'assets', 'graphs', 'genderGraph.png') # Define o caminho do gráfico
            plt.savefig(graph_path) # Salva o gráfico no caminho especificado (diretório local)

            graphLayout(plt).settings(title="Porcentagem de Gênero") # Configurações do gráfico

            plt.show() # Exibe o gráfico

            return True
        except:
            return False