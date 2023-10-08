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

        # Assegura que o gráfico de pizza seja um círculo.
        self.plt.axis('equal')

        self.plt.title(title)  # Define o título do gráfico

    # Configurações do gráfico de barras
    def bar(self, title):
        self.plt.title(title)
