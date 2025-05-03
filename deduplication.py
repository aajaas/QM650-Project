import pandas as pd
import numpy as np
from utils import output_path

def handle_duplicates(df):
    choice = input("\n🔍 Do you want to check for potential duplicate rows? (y/n): ").strip().lower()
    if choice != 'y':
        print("\n👌 Skipping duplicate check.")
        return df

    def extract_order_number(value):
        try:
            return int(str(value).split('-')[1])
        except (IndexError, ValueError):
            return np.nan

    df['order_num'] = df['web-scraper-order'].apply(extract_order_number)

    duplicate_indices = []
    grouped = df.groupby(['price', 'size', 'price per foot', 'location', 'classification'])

    for _, group in grouped:
        if len(group) < 2:
            continue

        group = group.sort_values(by='order_num')
        indices = group.index.tolist()

        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                idx1, idx2 = indices[i], indices[j]
                order_diff = abs(df.at[idx1, 'order_num'] - df.at[idx2, 'order_num'])

                if order_diff > 5:
                    duplicate_indices.extend([idx1, idx2])

    duplicate_indices = list(set(duplicate_indices))
    duplicate_rows = df.loc[duplicate_indices]

    if len(duplicate_rows) == 0:
        print("\n👌 No duplicates found.")
        return df

    print(f"\n🔁 Found {len(duplicate_rows)} potential duplicate rows.")
    next_action = input("Do you want to (d)isplay them, (r)emove them, or (n)othing? [d/r/n]: ").strip().lower()

    if next_action == 'd':
        print("\n--- Duplicate Rows ---")
        print(duplicate_rows.to_string(index=False))
        if input("\nDelete these duplicates? (y/n): ").strip().lower() == 'y':
            df = df.drop(duplicate_rows.index).reset_index(drop=True)
            df.to_csv(output_path, index=False)
            print(f"\n✅ Duplicates removed. Updated output written to: {output_path}")
    elif next_action == 'r':
        df = df.drop(duplicate_rows.index).reset_index(drop=True)
        df.to_csv(output_path, index=False)
        print(f"\n✅ Duplicates removed. Updated output written to: {output_path}")
    else:
        print("\n👌 No action taken.")

    # Clean up temp column
    df.drop(columns=['order_num'], inplace=True, errors='ignore')

    return df
