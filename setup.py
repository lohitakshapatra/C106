import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path)as csv_file:
      df=csv.DictReader(csv_file)
      fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
      fig.show()
def getDataSource(data_path):
    ice_cream_sales=[]
    temperature=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Ice-cream Sales"]))
            temperature.append(float(row["Temperature"]))
    return{"x":ice_cream_sales,"y":temperature}
def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between temp. vs ice cream sales",correlation[0,1])
def setup():
    data_path="temperature.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)  
    plotFigure(data_path)

setup()    
      
     
