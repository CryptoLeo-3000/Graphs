from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas, time

mycsv = pandas.read_csv("adbe.csv", parse_dates = ["Date"])

fig = figure(width = 500, height = 500, x_axis_type = "datetime")

fig.line(mycsv["Date"], mycsv["Close"], color = "Orange", alpha = 0.5)

output_file("TimeSeries.html")

show(fig)