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