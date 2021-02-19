from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#Values for x and y axis
dataframe = pandas.read_excel("TempPres.xlsx")
Temperature = dataframe["Temperature"]/10
pressure = dataframe["Pressure"]/10

#Output File
output_file("WeatherGraph.html")

#Figure Object
fig = figure(plot_width = 500, plot_height = 400, tools = "pan")

#Create Line Plot
fig.scatter(Temperature, pressure, size = 0.5)

#Graph Output
show(fig)