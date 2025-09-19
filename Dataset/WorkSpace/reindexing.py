import pandas as pd

def reindex_column_two(file_path, output_path="image_class_labels_updated.csv"):
    # Read CSV (no headers, 2 columns)
    df = pd.read_csv(file_path, header=None)
    
    # Get unique values in column 2 (sorted)
    unique_vals = sorted(df[1].unique())
    
    # Replace with ordered numbers
    for new_num, old_val in enumerate(unique_vals, start=1):
        df[1] = df[1].replace(old_val, new_num)
    
    # Save updated file
    df.to_csv(output_path, index=False, header=False)
    return output_path

# Example usage:
reindex_column_two("image_class_labels_updated.csv")