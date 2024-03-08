#9. 3D Plots using Plotly Libraries.

import plotly.graph_objects as go
import pandas as pd
import seaborn as sns

tips=sns.load_dataset("tips")

fig=go.Figure()

scatter=go.Scatter3d(
    x=tips['total_bill'],
    y=tips['tip'],
    z=tips['size'],
    mode='markers',
    marker=dict(size=8, color=tips['size'], colorscale='Viridis', opacity=0.8)
)

fig.add_trace(scatter)
fig.update_layout(dict(scene=dict(xaxis_title='Total Bill', yaxis_title='Tip', zaxis_title='Size'),title='3D Scatter Plot with Tips dataset'))


fig.write_html("3d_scatter_plot_tips.html")