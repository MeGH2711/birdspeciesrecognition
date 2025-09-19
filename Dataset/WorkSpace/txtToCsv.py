import pandas as pd

# Read txt file (split on space or :)
df = pd.read_csv("images.txt", sep=r"\s+|:", engine="python", header=None)

# Rename columns
df.columns = ["Value1", "Value2"]

# Save as CSV
df.to_csv("images.csv", index=False)