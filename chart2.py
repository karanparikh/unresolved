import pygal
from pygal.style import LightStyle

chart = pygal.Bar(title = "Research papers read per month", x_title = "Month", y_title = "Paper read", style = LightStyle)  

chart.x_labels = "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept"

chart.add("Expected", [3] * 9)
chart.add("Actual", [1, 1, 0, 0, 0, 0, 2, 2, 1])

chart.render_to_file("chart2.svg") 
