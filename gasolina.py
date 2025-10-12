from ctypes import py_object
import pandas as pd

gasolina_df = pd.read_csv('gasolina.csv',sep=',')

import seaborn as sns
from matplotlib import pyplot as plt

grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette='pastel')
plt.savefig('gasolina.png')
