import pygal
from pygal.style import LightStyle

chart = pygal.Bar(title = "Go learning progress", x_title = "Month", y_title = "Percentage learnt", style = LightStyle)  

chart.x_labels = "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept"

chart.add("Expected", [8.3] * 9)
chart.add("Actual", [5, 5, 0, 0, 0, 0, 0, 0, 0])

chart.render_to_file("chart1.svg") 