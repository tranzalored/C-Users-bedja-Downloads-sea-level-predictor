import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv",float_precision='legacy')


    # Create scatter plot
    plt.scatter(x='Year',y='CSIRO Adjusted Sea Level',data=df)


    # Create first line of best fit
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    res=linregress(x,y)
    year_extended = list(range(1880, 2050, 1))
    line = [res.intercept + res.slope * j for j in year_extended]
    plt.plot(year_extended, line, linewidth=2, color="r")



    # Create second line of best fit
    df1=df.copy()
    df1 = df1[df1['Year']>=2000]
    x1=df1['Year']
    y1=df1['CSIRO Adjusted Sea Level']
    res1=linregress(x1,y1)
    year_extended1 = list(range(2000, 2050, 1))
    line1 = [res1.intercept + res1.slope * j for j in year_extended1]
    plt.plot(year_extended1, line1, linewidth=2, color="k")


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()