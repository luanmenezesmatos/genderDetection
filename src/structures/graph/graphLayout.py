from matplotlib import font_manager

import os


class graphLayout:
    def __init__(self, plt=None):
        self.plt = plt

    def apply_font(self):
        fonts_path = os.path.join(os.getcwd(), 'src', 'assets', 'fonts')
        fonts_files = font_manager.findSystemFonts(fontpaths=fonts_path)

        for file in fonts_files:
            font_manager.fontManager.addfont(file)

    # Configurações do gráfico de pizza
    def pie(self, sizes, explode, labels, colors, title):
        # Criar um gráfico de pizza
        self.plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
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

        # Importar a função para manipular fontes
        self.apply_font()

        # Importar a função para definir os parâmetros do gráfico
        self.params(type='pie', bold_title=False, medium_title=True)

        # Assegura que o gráfico de pizza seja um círculo.
        self.plt.axis('equal')

        # Define o título do gráfico
        self.plt.title(title)

        # Inserir legenda no gráfico
        self.plt.legend(labels, title='Gênero', loc='best')

    # Configurações do gráfico de barras
    def bar(self, title):
        self.plt.title(title)

    def params(self, type, bold_title=False, medium_title=False, legend_size=10, bold_legend='normal', title_size=16):
        if type == 'pie':
            """ self.plt.rcParams['font.family'] = 'Roboto' # Define a fonte do gráfico
            # Aumentando o tamanho do título do gráfico
            self.plt.rcParams['axes.titlesize'] = 20

            # Alterar o estilo das fontes (bold) para os títulos e legendas do gráfico
            # Alterando o peso da fonte do título do eixo X e Y
            self.plt.rcParams['axes.labelweight'] = 'bold'
            # Alterando o peso da fonte do título do gráfico
            self.plt.rcParams['axes.titleweight'] = 'bold'
            # Alterando o tamanho da fonte da legendas
            self.plt.rcParams['legend.fontsize'] = 'large' """

            # Alterando o tamanho da figura (largura, altura)
            self.plt.rcParams['figure.figsize'] = (13, 7)

            self.plt.rcParams['font.family'] = 'Roboto' # Define a fonte do gráfico

            self.plt.rcParams['axes.titlesize'] = title_size # Define o tamanho do título do gráfico

            # Alterar o estilo das fontes (bold) para os títulos e legendas do gráfico
            # Alterando o peso da fonte do título do gráfico
            self.plt.rcParams['axes.titleweight'] = 'bold' if bold_title else 'normal' or 'medium' if medium_title else 'normal'
            # Alterando o tamanho da fonte da legendas
            self.plt.rcParams['legend.fontsize'] = legend_size if legend_size != 'large' else 'large' if bold_legend else 'medium' # Caso o tamanho da legenda seja 'large', então o peso da fonte será 'large' se não, será 'medium'
        elif type == 'bar':
            # Ainda irá fazer a configuração do gráfico de barras
            pass