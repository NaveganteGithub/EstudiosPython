import pandas as pd
import matplotlib.pyplot as mp

ventas = pd.read_csv('Tarea2\\company_sales.csv', sep=',').loc[:, 'month_number':'moisturizer']
ventas_DataFrame = pd.DataFrame(ventas)

region, axes = mp.subplots()

ventas_DataFrame.plot(x="month_number", y=['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer'], ax=axes)

mp.show()