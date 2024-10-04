import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

COLS = {
    "year": "Year",
    "csiro": "CSIRO Adjusted Sea Level",
    "lower": "Lower Error Bound",
    "upper": "Upper Error Bound",
    "noaa": "NOAA Adjusted Sea Level",
}

# Read data from file
df = pd.read_csv("epa-sea-level.csv")


def draw_plot():
    # Create scatter plot
    plt.scatter(x=df[COLS["year"]], y=df[COLS["csiro"]])

    # Create first line of best fit
    x = df[COLS["year"]].values
    y = df[COLS["csiro"]].values

    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    extended_x = np.arange(x.min(), 2051)
    line = slope * extended_x + intercept

    plt.plot(extended_x, line, color="green")

    # Create second line of best fit
    x = df[df[COLS["year"]] >= 2000][COLS["year"]].values
    y = df[df[COLS["year"]] >= 2000][COLS["csiro"]].values

    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    extended_x = np.arange(x.min(), 2051)
    line = slope * extended_x + intercept

    plt.plot(extended_x, line, color="red")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
