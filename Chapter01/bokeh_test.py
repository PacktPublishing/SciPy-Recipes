import numpy as np
from bokeh.plotting import figure, show

xvalues = np.linspace(-np.pi, np.pi, 50)
y1values = np.sin(xvalues)
y2values = np.cos(xvalues)

p = figure(
        tools='pan,box_zoom,reset',
        title='Trigonometric functions',
        x_axis_label='x',
        y_axis_label='y' 
    )

p.line(xvalues, y1values,
    legend='y=sin(x)', line_color='blue')
p.circle(xvalues, y2values, 
    legend='y=cos(x)', fill_color='green', 
    line_color='green', size=3)

show(p)

print('Plot generated. Open file bokeh_test.html on your browser.')
