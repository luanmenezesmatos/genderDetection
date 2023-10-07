class graphLayout:
    def __init__(self, plt):
        self.plt = plt

    # Configurações do gráfico
    def settings(self, title):
        # Define o título do gráfico
        self.plt.title(title)