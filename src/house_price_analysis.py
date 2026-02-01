import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Get the directory of the current script, then go up one level to data
data_path = Path(__file__).parent.parent / "data" / "house_price.csv"
df = pd.read_csv(data_path)

# -----------------------------------------------------------------------------
# Get basic info about the dataframe
# -----------------------------------------------------------------------------

#print(df.head())
#print(df.info())
#print(df.describe())
#print(f"Number of duplicate rows: {df.duplicated().sum()}")

print(f"Median house price: ${df['price'].median():,.2f}")
print(f"Average house price: ${df['price'].mean():,.2f}")
print(f"Minimum house price: ${df['price'].min():,.2f}")
print(f"Maximum house price: ${df['price'].max():,.2f}")

# -----------------------------------------------------------------------------
# Styles
# -----------------------------------------------------------------------------

label_font = {"fontsize": 15,
              "family": "sans-serif",
              "fontweight": "light",
              "color": "teal"}
title_font = {"fontsize": 15,
              "family": "sans-serif",
              "fontweight": "bold",
              "color": "teal"}
grid_style = {"color": "lightgray",
              "linestyle": "--",
              "linewidth": 0.7,
              "alpha": 0.7,
              "axis": "y"}

#------------------------------------------------------------------------------
# Analyze house prices by number of bedrooms
# -----------------------------------------------------------------------------

# Group by number of bedrooms and calculate average price
df_price_bedrooms = df.groupby("bedrooms")["price"].mean()

print("Average House Price by Number of Bedrooms:")
print(df_price_bedrooms.apply(lambda x: f"${x:,.2f}")) # format as currency

# Plot average house price by number of bedrooms
df_price_bedrooms.plot(kind="bar")
plt.title("Average House Price by Number of Bedrooms", **title_font)
plt.xlabel("Number of Bedrooms", **label_font)
plt.ylabel("Average Price ($M)", **label_font)
plt.xticks(rotation=0)
plt.yticks(np.arange(0, 6000001, 500000))
plt.grid(**grid_style)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# Analyze house prices by area
# -----------------------------------------------------------------------------

# Create area categories using quantiles
df["area_category"] = pd.qcut(df['area'], q=4, labels=['Small', 'Medium', 'Large', 'Very Large'])

# Group by area category and calculate average price
grouped_area = df.groupby('area_category')['price'].mean().reset_index()

# Sort area categories for better visualization
df_area = grouped_area.set_index('area_category').sort_index()

print("Average House Price by Area Category:")
print(df_area.apply(lambda x: f"${x['price']:,.2f}", axis=1))

# Plot average house price by area category using quantiles
grouped_area.plot(kind="bar",
                  x="area_category",
                  y="price")
plt.title("House Price by Area", **title_font)
plt.xlabel("Area Category", **label_font)
plt.ylabel("Price ($M)", **label_font)
plt.xticks(rotation=0)
plt.yticks(np.arange(0, 7000001, 500000))
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# Analyze house prices by furnishing status
# -----------------------------------------------------------------------------

# Group by furnishing status and calculate average price
df_furnished = df.groupby("furnishingstatus")["price"].mean()

# Sort values for better visualization
df_furnished = df_furnished.sort_values(ascending=True)

print("Average House Price by Furnishing Status:")
print(df_furnished.apply(lambda x: f"${x:,.2f}")) # format as currency

# Plot average house price by furnishing status
df_furnished.plot(kind="bar")
plt.title("Average House Price by Furnishing Status", **title_font)
plt.xlabel("Furnishing Status", **label_font)
plt.ylabel("Average Price ($M)", **label_font)
plt.xticks(rotation=0)
plt.yticks(np.arange(0, 6000001, 500000))
plt.tight_layout()
plt.show()