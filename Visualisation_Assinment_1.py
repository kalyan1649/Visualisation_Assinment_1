# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:38:52 2023

@author: Sai Kalyan
"""
"""
Importing pandas and matplotlib.pyplot modules for help in 
read the excel file and plot the graphs using the required 
data and create various types of graphs and plots with our data
"""
import pandas as pd # importing pandas as pd
import matplotlib.pyplot as plt # importing plypolt from matplotlib

# read file into dataframe and printing the DataFrame
line_gds = pd.read_excel("line.xlsx")
print(line_gds) # print line graph data
#Defining the Function for plotting Line plot.
def Linegraph(Countrie1,Countrie2,Countrie3,Countrie4,) :

    """"Plotting four countries with labels"""
    plt.figure()
    plt.plot(line_gds["PERIOD"], line_gds[Countrie1], label=Countrie1)
    plt.plot(line_gds["PERIOD"], line_gds[Countrie2], label=Countrie2)
    plt.plot(line_gds["PERIOD"], line_gds[Countrie3], label=Countrie3)
    plt.plot(line_gds["PERIOD"], line_gds[Countrie4], label=Countrie4)
    
    #Setting the labels and showing the legends
    plt.xlim(2005,2014) # setting x-limit
    plt.ylim(5,85) # setting y-limit
    plt.xlabel("% of GDP from 2005 to 2014") #labelling x-axis
    plt.ylabel("% of GDP") #labelling y-axis
    plt.title("Percentage of GDP through Exports of goods and services") 
    plt.legend(title="COUNTRIES",edgecolor = "blue")#coloring the boundary
    plt.savefig("LinePlot.png")#Saving the line plot
    plt.show()
    return #returing the function
#Function for plotting Bar Graph
def Bargraph(Breadth,Height):
    
    Population_growth = pd.read_excel("bar.xlsx")
    print(Population_growth)#print barchat values
    """Plotting countries with labels"""
    plt.figure(figsize=(Breadth,Height))# here Breadth and Height can be called by the function
    Population_growth.plot(x='Period', kind='bar')
    
    #Setting labels and showing the legends
    plt.ylim(0,2.9)
    plt.title('Population growth annual %')
    plt.xlabel("Years From 2001 to 2005")
    plt.ylabel("% of Annual")
    plt.legend(title="COUNTRIESS",edgecolor = "Blue",loc = "upper right")
    plt.show()
    return #returing the function
#Function for plotting Pie Chart
def PieGraph(Agricultural_land ,PERIOD):

    land_per= pd.read_excel("Agricultral_land.xlsx")
    print(land_per)
    
    # pie chart for the seven countries
    """Plotting pie chart for with for the countries"""
    plt.figure()
    plt.pie(land_per[Agricultural_land], labels = land_per['COUNTRY'], autopct='%1.1f%%' , pctdistance = 0.5 , 
       labeldistance = 1.1,wedgeprops = {'linewidth' : 1.0,'edgecolor' : 'white'} )
    
    plt.title("Agricultural land % of land area " + PERIOD)
    plt.show()
    return  #returing the function
Linegraph("Thailand","Finland","Zimbabwe","Japan") #Calling the defined function for Line Plot
Bargraph(10,8) # Calling the defined function for Bar Plot
PieGraph("Agricultural_land in 2015","2015")#Calling defined function for Pie Chart of the Year 2007
PieGraph("Agricultural_land in 2021","2021")#Calling defined function for Pie Chart of the Year 2021
