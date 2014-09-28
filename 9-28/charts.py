import pygal

X_LABELS = "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept"

def generate_chart_1():
  chart = pygal.Bar(title = "Go learning progress", x_title = "Month", y_title = "Percentage learnt" )  

  chart.x_labels = X_LABELS

  chart.add("Expected", [8.3] * 9)
  chart.add("Actual", [5, 5, 0, 0, 0, 0, 0, 0, 40])

  chart.render_to_file("chart1.svg") 

generate_chart_1()
