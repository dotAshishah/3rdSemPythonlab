# 8B. PLOTTING DIFFERENT TYPES OF PLOTS USING BOKEH

import pandas as pd
import numpy as np
from bokeh.plotting import output_file,figure,show
from bokeh.plotting import gridplot
import seaborn as sns
tips=sns.load_dataset("tips")
output_file("bokeh_tips_plots.html")

hist,edges=np.histogram(tips['total_bill'], bins=8)
hist_plot=figure(title="Histogram of total Bill", x_axis_label="Total Bill", y_axis_label="Frequency")
hist_plot.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="purple", line_color="white")

day_categories = sorted(tips['day'].unique())
average_total_bill=tips.groupby('day')['total_bill'].mean()
bar_plot=figure(title="Average Total Bill per Day", x_axis_label='Day', y_axis_label='Average Total Bill', x_range=day_categories)
bar_plot.vbar(x=day_categories, top=average_total_bill, width=0.5, color="orange")

scatter_plot=figure(title="Scatter Plot of Total Bill vs Tip", x_axis_label='Total Bill', y_axis_label='Tip')
scatter_plot.scatter(x='total_bill', y='tip', size=8, color='green', alpha=0.6, source=tips)

plots=gridplot([[hist_plot,bar_plot],[scatter_plot]])
show(plots)