import pandas as pd

def calculate_missing_price_per_foot(df):
    for i, row in df.iterrows():
        if pd.isnull(row['price per foot']) and row['size'] > 0:
            size_sqft = row['size'] * 10.7639
            df.at[i, 'price per foot'] = round(row['price'] / size_sqft, 1)

def check_price_errors(df):
    price_errors = []
    for i, row in df.iterrows():
        price = row['price']
        if price < 1000:
            size_sqft = row['size'] * 10.7639
            if price <= 99:
                corrected_price = price * size_sqft
            elif price <= 999:
                corrected_price = price * 1000
            else:
                continue
            corrected_price_per_foot = round(corrected_price / size_sqft, 1)
            price_errors.append({
                'index': i,
                'old_price': price,
                'new_price': corrected_price,
                'old_price_per_foot': row['price per foot'],
                'new_price_per_foot': corrected_price_per_foot
            })
    return price_errors

def handle_price_corrections(df, price_errors):
    if not price_errors:
        return df

    import pandas as pd
    print("\n⚠️ Price Errors Detected:")
    error_df = pd.DataFrame(price_errors)
    print("\n--- Affected Rows ---")
    print(error_df[['index', 'old_price', 'new_price', 'old_price_per_foot', 'new_price_per_foot']].to_string(index=False))

    action = input("\nDo you want to (o)verwrite the old values with the corrected values, or (k)eep the original ones? [o/k]: ").strip().lower()
    if action == 'o':
        for error in price_errors:
            df.at[error['index'], 'price'] = error['new_price']
            df.at[error['index'], 'price per foot'] = error['new_price_per_foot']
        print("\n✅ Price values overwritten with corrected values.")
    else:
        print("\n👌 Keeping original price values.")
    return df
