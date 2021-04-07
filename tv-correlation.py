import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
  size_of_tv = []
  hours_spent= []

  with open(data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      size_of_tv.append(float(row["Size of TV"]))
      hours_spent.append(float(row["sleep"]))
  return {"x": size_of_tv, "y":hours_spent}

def find_Correlation(data_source):
  correlation = np.corrcoef(data_source["x"],data_source["y"])
  print("Correlation between Size Of Tv V/S Average time spent watching TV in a week (hours) :-\n--->",correlation[0,1])

def setup():
  data_path = "tv.csv"
  data_source = getDataSource(data_path)
  find_Correlation(data_source)

setup()      