import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df = pd.read_csv('Files/epa-sea-level.csv')
    # Create scatter plot
    y_value = df['CSIRO Adjusted Sea Level']
    x_value = df['Year']
    fig, ax = plt.subplots()
    plt.scatter(x_value,y_value, c = y_value, cmap= plt.cm.Blues)

    # Create first line of best fit
    res = linregress(x_value,y_value)
    pred_x = pd.Series(i for i in range(1880, 2051))
    pred_y = res.slope*pred_x + res.intercept #MX + B, slope*X plus y intercept
    plt.plot(pred_x, pred_y, c = 'purple', )


    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']
    res2 = linregress(x2,y2)
    pred_x2 = pd.Series(i for i in range(2000,2051))
    pred_y2 = res2.slope*pred_x2 + res2.intercept
    plt.plot(pred_x2, pred_y2, c = 'r')
    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel('Sea level (in)')
    ax.set_title("Rise in sea level")
    
    
    plt.savefig('sea_level_plot.png')
    # return plt.gca()

draw_plot()