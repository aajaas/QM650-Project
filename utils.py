import os
import re
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
raw1_path = os.path.join(script_dir, 'Raw_data', 'propartfinder2.csv')
raw2_path = os.path.join(script_dir, 'Raw_data', 'BahrainFinder.csv')
output_dir = os.path.join(script_dir, 'Cleaned_data')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'output.csv')

valid_classifications = {
    "RA", "RB", "RG", "RHB", "RHA", "B3*", "SP", "BD", "B4", "UNDEFINED", "BC",
    "B3", "LD", "BB", "BA", "S", "MOH", "RB*", "COM", "WS", "GB", "AG", "BR5", "DB", "RAC"
}
classification_regex = re.compile(r'\b(' + '|'.join(re.escape(c) for c in valid_classifications) + r')\b', re.IGNORECASE)

def print_progress(current, total, bar_length=40):
    percent = float(current) / total
    arrow = '=' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write(f'\rProgress: [{arrow + spaces}] {int(percent * 100)}% ({total - current} remaining)')
    sys.stdout.flush()
