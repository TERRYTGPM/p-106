import plotly.express as px
import csv
import numpy

def e(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    temp = []
    sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for rows in csv_reader:
            temp.append(float(rows["Marks In Percentage"]))
            sales.append(float(rows["Ice-cream Sales"]))

    return {"x" : temp, "y": sales}

def correlation(data_source):
    correlation = numpy.corrcoef(data_source["x"], data_source["y"])

def main():
    data_path  = "./data/Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    correlation(datasource)
    e(data_path)

main()