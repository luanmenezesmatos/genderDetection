import pandas as pd
from matplotlib import pyplot as plt

from src.structures.graph.genderGraph import genderGraph

class HandleGraph:
    def __init__(self, predictions):
        self.predictions = predictions

    def dataProcessing(self):
        # Criar um dataframe
        dataframe = pd.DataFrame(self.predictions)

        genderGraph(dataframe).generate()