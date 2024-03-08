# 8A. BOKEH LINE GRAPH USING ANNOTATIONS AND LEGENDS

from bokeh.plotting import figure,output_file,show
from bokeh.models import Label

x=[1,2,3,4,5]
y=[2,4,6,8,10]
output_file("line_graph_with_annotations.html")
p=figure(title="Bokeh line Graph with Annotations", x_axis_label='X-axis', y_axis_label='Y-axis')
p.line(x,y,line_width=2,line_color="blue",legend_label="Line Function: y=2x")
annotation=Label(x=3,y=6,text="Important Point", text_font_size="10pt", text_color="red")
p.add_layout(annotation)
p.legend.location="top_left"
p.legend.click_policy="hide"
show(p)