# pip install pandas
# pip install matplotlib
# pip install seaborn
# pip install plotly

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# загрузка данных
dataSet = pd.read_csv("visualization_comparison_data.csv")
dataSet['Date'] = pd.to_datetime(dataSet['Date'])  # преобразование даты

# matplotlib визуализации
def plotMatplotlib(dataSet):
    plt.figure(figsize=(14, 8))

    # линейный график
    plt.subplot(2, 2, 1)
    plt.plot(dataSet['Date'], dataSet['Sales'], marker='o', linestyle='-', label='Sales')
    plt.title("Matplotlib: линейный график продаж")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.legend()

    # гистограмма
    plt.subplot(2, 2, 2)
    plt.hist(dataSet['Profit'], bins=10, color='skyblue', edgecolor='black')
    plt.title("Matplotlib: гистограмма прибыли")
    plt.xlabel("Profit")
    plt.ylabel("Frequency")

    # точечный график
    plt.subplot(2, 2, 3)
    colorMap = {'A': 'red', 'B': 'blue', 'C': 'green'}
    plt.scatter(dataSet['Sales'], dataSet['Profit'], c=dataSet['Category'].map(colorMap), label="Categories")
    plt.title("Matplotlib: точечный график")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.legend(colorMap, title="Category")

    plt.tight_layout()
    plt.show()

# seaborn визуализации
def plotSeaborn(dataSet):
    plt.figure(figsize=(14, 8))

    # линейный график
    plt.subplot(2, 2, 1)
    sns.lineplot(data=dataSet, x='Date', y='Sales', marker='o', label='Sales')
    plt.title("Seaborn: линейный график продаж")
    plt.xticks(rotation=45)

    # гистограмма
    plt.subplot(2, 2, 2)
    sns.histplot(dataSet['Profit'], kde=True, bins=10, color='purple')
    plt.title("Seaborn: гистограмма прибыли")

    # точечный график
    plt.subplot(2, 2, 3)
    sns.scatterplot(data=dataSet, x='Sales', y='Profit', hue='Category', palette='deep', s=100)
    plt.title("Seaborn: точечный график")

    plt.tight_layout()
    plt.show()

# plotly визуализации
def plotPlotly(dataSet):
    # линейный график
    figLinePlotly = px.line(dataSet, x='Date', y='Sales', title="Plotly: линейный график продаж")
    figLinePlotly.show()

    # гистограмма
    figHistPlotly = px.histogram(dataSet, x='Profit', nbins=10, title="Plotly: гистограмма прибыли", color_discrete_sequence=['orange'])
    figHistPlotly.show()

    # точечный график
    figScatterPlotly = px.scatter(dataSet, x='Sales', y='Profit', color='Category', size='Profit',
                                  title="Plotly: точечный график", hover_data=['Category'])
    figScatterPlotly.show()

# вызов функций
plotMatplotlib(dataSet)
plotSeaborn(dataSet)
plotPlotly(dataSet)
