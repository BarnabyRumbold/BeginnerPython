import pandas as pd
import numpy as np
import matplotlib

data=pd.read_csv(r"C:\Users\Barna\OneDrive\Desktop\Air_Quality.csv")
print(data.head(50))
#print(len(data))
#print(data.columns)
##print(data["Time Period"])
print(data["Measure Info"].head())