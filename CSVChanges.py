import pandas

csvfile = pandas.read_csv("bachelors.csv")

sheet = csvfile['bachelors']
newcell = sheet['U']