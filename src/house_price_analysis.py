import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Get the directory of the current script, then go up one level to data
data_path = Path(__file__).parent.parent / "data" / "house_price.csv"
df = pd.read_csv(data_path)