import pandas as pd

# Read the CSV
df = pd.read_csv("images.csv")

# Save as space-separated TXT
df.to_csv("images.txt", sep=" ", index=False, header=False)