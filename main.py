from data_loader import load_property_finder_data, load_bahrain_finder_data
from processing import calculate_missing_price_per_foot, check_price_errors, handle_price_corrections
from deduplication import handle_duplicates
from utils import output_path

import pandas as pd

# Load data
df1 = load_property_finder_data()
df2 = load_bahrain_finder_data()

# Combine
final_df = pd.DataFrame(df1 + df2)

# Fill missing values
calculate_missing_price_per_foot(final_df)

# Save output
final_df.to_csv(output_path, index=False)
print(f"\n\n✅ Done! Combined output written to: {output_path}")

# Check for price errors
price_errors = check_price_errors(final_df)
final_df = handle_price_corrections(final_df, price_errors)

# Check for duplicates
final_df = handle_duplicates(final_df)