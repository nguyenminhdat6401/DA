import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (using all data)
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    ax.plot(
        years_extended,
        intercept + slope * years_extended,
        'r',
        label='Best fit: 1880-2050',
    )

    # Create second line of best fit (from year 2000 onward)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(
        years_recent,
        intercept2 + slope2 * years_recent,
        'green',
        label='Best fit: 2000-2050',
    )

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
