# 4. b) Write a Python program to Demonstrate how to draw a Scatter Plot using Matplotlib
# import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Importing data.
cars_data = pd.read_csv("Toyota.csv")
# Create scatter plot using two variables, Age and Price.
plt.scatter(cars_data['Age'],cars_data['Price'],c='blue')
# To set the title
plt.title('Scatter plot of Price vs Age of the Cars')
# To set the x and y axis labels.
plt.xlabel('Age (months)')
plt.ylabel('Price (Euros)')
# To show the scatter plot
plt.show()
