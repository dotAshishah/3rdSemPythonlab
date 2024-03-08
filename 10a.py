# 10A. Time Series using Plotly Libraries

import plotly.express as px
import pandas as pd

data = pd.read_csv("Rainfall_data.csv")

data['Date']=pd.to_datetime(data[['Year','Month','Day']])

fig = px.line(data, x='Date', y=['Temperature'],title='Time Series Plot', labels={'Temperature': 'Temperature (°C)'}, line_shape='linear')
fig.show()