# . a) Write a Python program to Demonstrate how to draw a Histogram using Matplotlib
# import the necessary libraries
# Pandas library for data frames
import pandas as pd
# numpy library to do numerical operations
import numpy as np
import matplotlib.pyplot as plt
cars_data = pd.read_csv("cars.csv")
plt.title('Histogram for distance travelled in KiloMeter')
plt.hist(cars_data ['KM'], color='green', edgecolor='white', bins=5)
plt.xlabel('Kilometer')
plt.ylabel('Frequency')
plt.show()
