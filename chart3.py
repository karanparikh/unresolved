import pygal
from pygal.style import LightStyle

chart = pygal.Bar(title = "Blog posts per month", x_title = "Month", y_title = "Posts written", style = LightStyle)  

chart.x_labels = "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept"

chart.add("Expected", [4] * 9)
chart.add("Actual", [3, 2, 3, 0, 1, 2, 2, 0, 2])

chart.render_to_file("chart3.svg") 