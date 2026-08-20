import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Clear the current figure to prevent test interference
    plt.clf()

    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope_all, intercept_all, r_val, p_val, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(1880, 2051))
    fit_all = slope_all * years_all + intercept_all
    plt.plot(years_all, fit_all, 'r')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_rec, intercept_rec, r_val, p_val, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_rec = pd.Series(range(2000, 2051))
    fit_rec = slope_rec * years_rec + intercept_rec
    plt.plot(years_rec, fit_rec, 'green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()