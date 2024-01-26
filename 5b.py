# . b) Write a Python program to Demonstrate how to draw a Piechart using Matplotlib
# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
# Creating dataset
cars_data = pd.read_csv("Car_BarPlot.csv")
cars = cars_data["Car"]
data = cars_data["Sales"]
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = cars)
# show plot
plt.show()
