# -*- coding: utf-8 -*-
"""Apredendo Seaborn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vYJ2t6U11dFk3tfunmmz_IDfTlpBBUm1

# Importação das bibliotecas
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""importação da base de dados"""

videos_df = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/datapython2413/05-Exercicio de Seaborn/videosYT.xlsx', 'videos')
display(videos_df)

"""Criação de gráfico de dispersão"""

fig = sns.scatterplot(data=videos_df , x='Nº de Views', y='Nº de Likes', hue= 'Responsável', style='Responsável', palette=['red', 'black'])
plt.show(fig)

"""# Criando gráfico de dispersão relacional"""

grafico_relacional = sns.relplot(data=videos_df, x='Nº de Views', y='Nº de Likes', hue='Categoria', col='Responsável')
grafico_relacional.set_titles('O responsável por esse gráfico é o/a {col_name}')
plt.show(grafico_relacional)

"""# **Criando gráfico de linha**




"""

inscritos_df = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/datapython2413/05-Exercicio de Seaborn/videosYT.xlsx', 'Inscritos')
display(inscritos_df)

graf_linha = sns.lineplot(data=inscritos_df, x='Mês/Ano', y='Inscritos', color = 'red')
plt.show(graf_linha)

"""# Criando Gráficos de Histograma- Modelo 1"""

fig = sns.histplot(data=videos_df, x='Nº de Views')
plt.show(fig)

"""# Criando Gráficos de Histograma- Modelo 2"""

fig = sns.displot(data=videos_df, x='Nº de Views', hue='Responsável')
plt.show(fig)

"""# Criando Gráficos de Histograma- Modelo 3"""

fig = sns.displot(data=videos_df, x='Nº de Views', hue='Responsável', col = 'Responsável')
plt.show(fig)

"""# Criando Gráficos de Histograma- Modelo 4"""

fig = sns.displot(data=videos_df, x='Nº de Views', kind ='kde', hue= 'Responsável')
plt.show(fig)

"""# Criando Gráficos de Histograma- Modelo 5"""

fig = sns.displot(data=videos_df, x='Nº de Views', kind ='ecdf', hue= 'Responsável')
plt.show(fig)

"""# Criando uma Regressão Linear"""

graf_regressao = sns.regplot(data=videos_df, x='Nº de Views', y='Nº de Likes')
plt.show(graf_regressao)

"""Alterando uma regressão Linear"""

graf_regressao = sns.lmplot(data=videos_df, x='Nº de Views', y='Nº de Likes', hue='Responsável')
plt.show(graf_regressao)