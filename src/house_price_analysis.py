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
print(df.info())

#------------------------------------------------------------------------------
# Analyze house prices by number of bedrooms
# -----------------------------------------------------------------------------

# Group by number of bedrooms and calculate average price
df_price_bedrooms = df.groupby("bedrooms")["price"].mean()

# format y-axis as currency
print(df_price_bedrooms.apply(lambda x: f"${x:,.2f}"))

# Plot average house price by number of bedrooms
df_price_bedrooms.plot(kind="bar", 
                       title="Average House Price by Number of Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Average Price ($M)")
plt.yticks(np.arange(0, 6000001, 500000))
plt.xticks(rotation=0)
plt.grid(axis='y',
         linestyle='--',
         alpha=0.7)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------
# Analyze house prices by area
# -----------------------------------------------------------------------------

# Create area bins/ranges
df['area_category'] = pd.cut(df['area'], 
                             bins=[0, 5000, 7000, 11000, float('inf')], 
                             labels=['Small', 'Medium', 'Large', 'Very Large'])

# Group by area category and calculate average price
grouped_area = df.groupby('area_category')['price'].mean().reset_index()

# Plot average house price by area category
grouped_area.plot(kind="bar",
        x="area_category",
        y="price",
        title="House Price by Area")
plt.xlabel("Area Category")
plt.ylabel("Price ($M)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()