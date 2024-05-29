import pandas as pd
import numpy as np

# Load the Excel file
df = pd.read_csv("data/channel_list_1000.csv")

# List of verticals
verticals = ["Auto & Vehicles", "Sports Editorial Content", "Entertainment", "Kids Content", "Family", 
             "News, Politics, & Information", "Gaming", "Tech", "Education & Science", "Food & Drinks", 
             "Corporate Channels", "Lifestyle & Hobbies", "Health & Fitness"]

# Create a dataframe to store the split datasets
datasets = [pd.DataFrame() for _ in range(4)]

# For each vertical, split the rows equally among the four datasets
for vertical in verticals:
    vertical_df = df[df["vertical"] == vertical]
    split_dfs = np.array_split(vertical_df, 4)
    
    for i in range(4):
        datasets[i] = pd.concat([datasets[i], split_dfs[i]])

# Save each dataset to a CSV file
for i, dataset in enumerate(datasets):
    dataset.to_csv(f"dataset_{i+1}.csv", index=False)

print("Datasets have been split and saved successfully.")