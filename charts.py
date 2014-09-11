import pygal
from pygal.style import LightStyle

X_LABELS = "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept"

def generate_chart_1():
  chart = pygal.Bar(title = "Go learning progress", x_title = "Month", y_title = "Percentage learnt", style = LightStyle)  

  chart.x_labels = X_LABELS

  chart.add("Expected", [8.3] * 9)
  chart.add("Actual", [5, 5, 0, 0, 0, 0, 0, 0, 0])

  chart.render_to_file("chart1.svg") 

def generate_chart_2():
  chart = pygal.Bar(title = "Research papers read per month", x_title = "Month", y_title = "Paper read", style = LightStyle)  

  chart.x_labels = X_LABELS

  chart.add("Expected", [3] * 9)
  chart.add("Actual", [1, 1, 0, 0, 0, 0, 2, 2, 1])

  chart.render_to_file("chart2.svg") 

def generate_chart_3():
  chart = pygal.Bar(title = "Blog posts per month", x_title = "Month", y_title = "Posts written", style = LightStyle)  

  chart.x_labels = X_LABELS

  chart.add("Expected", [4] * 9)
  chart.add("Actual", [3, 2, 3, 0, 1, 2, 2, 0, 2])

  chart.render_to_file("chart3.svg") 

generate_chart_1()
generate_chart_2()
generate_chart_3()