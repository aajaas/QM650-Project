import pandas as pd
import re
from utils import raw1_path, raw2_path, print_progress, classification_regex

def load_property_finder_data():
    df1 = pd.read_csv(raw1_path)
    cleaned_rows = []

    for i, row in df1.iterrows():
        try:
            web_order = row['web-scraper-order']
            price = float(str(row['price']).replace(',', '').strip())
            location = str(row['location']).split(',')[0].strip()
            size_match = re.search(r'(\d+(?:,\d{3})*|\d+)\s*sqft\s*/\s*(\d+(?:,\d{3})*|\d+)\s*sqm', str(row['size']))
            size = float(size_match.group(2).replace(',', '')) if size_match else ''
            match_class = classification_regex.search(str(row['description']))
            classification = match_class.group(1).upper() if match_class else ''
            match_road = re.search(r'(\d+)\s+(?:road|roads)', str(row['description']), re.IGNORECASE)
            roads = int(match_road.group(1)) if match_road else 1
            price_per_foot = round(price / (size * 10.7639), 1) if size else ''

            cleaned_rows.append({
                'source': 'Property Finder',
                'web-scraper-order': web_order,
                'price': int(price),
                'size': size,
                'location': location,
                'classification': classification,
                'roads': roads,
                'price per foot': price_per_foot
            })

            print_progress(i + 1, len(df1))

        except Exception as e:
            print(f"\nError processing row {i}: {e}")
    return cleaned_rows

def load_bahrain_finder_data():
    df2 = pd.read_csv(raw2_path)
    bahrain_rows = []

    for _, row in df2.iterrows():
        try:
            price = int(float(str(row['price']).replace('BD', '').replace(',', '').strip()))
            price_per_foot = round(float(row['price per foot']), 1) if pd.notnull(row['price per foot']) else ''

            bahrain_rows.append({
                'source': 'Bahrain Finder',
                'web-scraper-order': row['web-scraper-order'],
                'price': price,
                'size': row['size'],
                'location': row['location'],
                'classification': row['classification'],
                'roads': row['roads'],
                'price per foot': price_per_foot
            })
        except Exception as e:
            print(f"\nError in BahrainFinder row: {e}")
    return bahrain_rows
