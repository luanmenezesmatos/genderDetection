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

    def add_font_entries(self):
        fonts_path = os.path.join(os.getcwd(), 'src', 'assets', 'fonts')

        if not os.path.exists(fonts_path):
            os.mkdir(fonts_path)

        # Pegar todos os nomes dos arquivos presentes na pasta e remover o .ttf de cada um
        fonts_files = [file.split('.')[0] for file in os.listdir(fonts_path)]
        
        # Adicionar as fontes
        for file in fonts_files:
            fe = font_manager.FontEntry(
                fname=os.path.join(fonts_path, f'{file}.ttf'),
                name=file
            )

            font_manager.fontManager.ttflist.insert(0, fe)


    # Configurações do gráfico de pizza
    def pie(self, sizes, explode, labels, colors, title):
        # Criar um gráfico de pizza
        """ self.plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                     shadow=True, startangle=140, pctdistance=0.85, wedgeprops={'edgecolor': 'black'}) """
        # sizes - Valores numéricos das fatias
        # explode - Define quais fatias serão explodidas
        # labels - Rótulos das fatias
        # colors - Cores das fatias
        # autopct - Formato de exibição dos valores numéricos
        # shadow - Ativa sombra
        # startangle - Define o ângulo inicial de exibição das fatias
        # pctdistance - Define a distância dos valores numéricos em relação ao centro do gráfico
        # wedgeprops - Define as propriedades das fatias (borda)

        # Importar a função para definir os parâmetros do gráfico
        self.params(type='pie', bold_title=True, bold_legend=True)

        # Assegura que o gráfico de pizza seja um círculo.
        self.plt.axis('equal')

        # Define o título do gráfico
        self.plt.title(title)

        # Inserir legenda no gráfico
        self.plt.legend(labels, title='Gênero', loc='best')

    # Configurações do gráfico de barras
    def bar(self, title):
        self.plt.title(title)

    def params(self, type, bold_title=False, medium_title=False, legend_size='large', bold_legend=False, title_size=16):
        if type == 'pie':
            # Importar a função para manipular fontes
            self.apply_font()
            self.add_font_entries()

            # Definindo a fonte do gráfico e o estilo
            self.plt.rcParams['font.family'] = 'Roboto-Regular'

            # Definindo o tamanho do título do gráfico
            self.plt.rcParams['axes.titlesize'] = title_size

            # Alterar o estilo das fontes (bold) para os títulos e legendas do gráfico
            # Alterando o peso da fonte do título do gráfico
            self.plt.rcParams['axes.titleweight'] = 'bold' if bold_title else 'normal' or 'medium' if medium_title else 'normal'
            # Alterando o tamanho da fonte da legendas
            self.plt.rcParams['legend.fontsize'] = legend_size if legend_size != 'large' else 'large' if bold_legend else 'medium' # Caso o tamanho da legenda seja 'large', então o peso da fonte será 'large' se não, será 'medium'
            self.plt.rcParams['legend.title_fontsize'] = 'large' if bold_legend else 'medium' # Caso o tamanho da legenda seja 'large', então o peso da fonte será 'large' se não, será 'medium'
        elif type == 'bar':
            # Importar a função para manipular fontes
            self.apply_font()
            self.add_font_entries()