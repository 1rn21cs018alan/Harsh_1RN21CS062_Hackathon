import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import plotly.graph_objects as go
import seaborn

filename="Data Analytics and ML/The_Case_of_the_Predictive_Crime_Solver.csv"
raw_data=pd.read_csv(filename)
print(raw_data.head())

# exit(0)
lattitude=raw_data['LAT']
longitude=raw_data['LON']

dates=pd.to_datetime(raw_data['DATE OCC'],format="%m/%d/%Y %H:%M")
crime_code=raw_data['Crm Cd']
# cleaning
longitude=longitude[lattitude!=0]
dates=dates[lattitude!=0]
crime_code=crime_code[lattitude!=0]
new_data=raw_data[lattitude!=0]
lattitude=lattitude[lattitude!=0]
print(new_data.columns)
# new_data['Date Rptd']=pd.to_datetime(new_data['Date Rptd'],format="%m/%d/%Y %H:%M").values.astype('float64')
temp=new_data['DATE OCC'].str.slice(0,-4)
def stringify(x):
    # print(x)
    val=x['TIME OCC']
    tim="%02d:%02d"%(int(val/100),val%100)
    return tim
temp2=new_data.apply(stringify,axis=1)
temp3=temp+temp2
# print(temp3)
# exit(0)
temp4=pd.to_datetime(temp3,format="%m/%d/%Y %H:%M").values.astype('float64')
# new_data['DATE OCC' ]=pd.to_datetime(new_data['DATE OCC' ],format="%m/%d/%Y %H:%M").values.astype('float64')
new_data['DATE OCC']=temp4.copy()
hash_to_str={"Vict Descent":{},"Vict Sex":{}} 
def to_str1(x):
    hash_to_str['Vict Sex'][x['Vict Sex']]=hash(x['Vict Sex'])
    return hash(x["Vict Sex"])    
def to_str2(x):
    hash_to_str["Vict Descent"][x["Vict Descent"]]=hash(x["Vict Descent"])
    return hash(x["Vict Descent"])
# new_data=new_data[['DATE OCC',"Date Rptd",'TIME OCC',"Crm Cd","Vict Age","Vict Sex","Vict Descent","LAT","LON"]]
new_data=new_data[['DATE OCC',"Crm Cd","Vict Age","Vict Sex","Vict Descent","LAT","LON"]]

new_data.dropna(subset=["Vict Sex","Vict Descent"], inplace=True)

new_data["Vict Sex"]    =new_data.apply(to_str1,axis=1)
new_data["Vict Descent"]=new_data.apply(to_str2,axis=1)
new_data=new_data.sort_values(by=['DATE OCC'])
seaborn.heatmap(data=new_data.corr(),annot=True)
plt.show()
plt.plot(new_data["DATE OCC"],new_data["Crm Cd"])
plt.xlabel("Date")
plt.ylabel("Crm Cd")
plt.show()
plt.scatter(new_data["DATE OCC"],new_data["Vict Age"])
plt.xlabel("Date")
plt.ylabel("Vict Age")
plt.show()
plt.scatter(new_data["DATE OCC"],new_data["Vict Sex"])
plt.xlabel("Date")
plt.ylabel("Vict Sex")
plt.show()
plt.scatter(new_data["DATE OCC"],new_data["Vict Descent"])
plt.xlabel("Date")
plt.ylabel("Vict Descent")
plt.show()
plt.scatter(new_data["DATE OCC"],new_data["LAT"])
plt.xlabel("Date")
plt.ylabel("LAT")
plt.show()
plt.scatter(new_data["DATE OCC"],new_data["LON"])
plt.xlabel("Date")
plt.ylabel("LON")
plt.show()
