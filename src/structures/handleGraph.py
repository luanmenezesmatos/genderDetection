from src.structures.graph.genderGraph import genderGraph
from src.structures.graph.raceGraph import raceGraph

import pandas as pd # Para trabalhar com dataframes
import os # Biblioteca para trabalhar com diretórios

appEnv = os.getenv('APP_ENV')

class HandleGraph:
    def __init__(self, predictions, app_environment=appEnv):
        self.predictions = predictions
        self.app_environment = app_environment

    def dataProcessing(self):
        if self.app_environment == 'development':
            dataframe = pd.DataFrame(self.predictions)

            genderGraph(dataframe).generate()
            raceGraph(dataframe).generate()
        elif self.app_environment == 'production':
            # Criar um dataframe
            dataframe = pd.DataFrame(self.predictions)

            genderGraph(dataframe).generate()
            raceGraph(dataframe).generate()