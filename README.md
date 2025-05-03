# Land Plot Pricing Analysis in Bahrain

## Project Overview

This project aims to statistically analyze the relationship between land plot pricing in Bahrain and several key factors. Specifically, it investigates the correlation between the **price per foot** (independent variable) and other variables such as **location**, **classification**, **number of roads**, and **availability in the area**.

### Objective

The goal of this project is to understand how various features influence land pricing and to develop a data-driven model that can predict pricing trends. This analysis is especially valuable for understanding real estate dynamics in Bahrain and can be applied to various fields like investment, urban planning, and property development.

## Data Sources

The project utilizes data from two primary sources:

- **Property Finder**: A popular property listing website.
- **Bahrain Finder**: A local real estate platform providing information about land plots available for sale in Bahrain.

Both datasets are cleaned, transformed, and analyzed to extract meaningful insights about land pricing.

## Files and Structure

The project is organized as follows:

- **raw_data**: Contains raw CSV files (`propartfinder2.csv`, `BahrainFinder.csv`) for both data sources.
- **cleaned_data**: Stores the cleaned and processed data in `output.csv`.
- **utils**: Includes utility functions for data processing and cleaning, such as price calculations and progress reporting.
- **deduplication.py**: A script to handle potential duplicates in the dataset by checking for similar rows based on multiple features and removing them as necessary.

## Installation

To use this project, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/land-plot-pricing-bahrain.git
   cd land-plot-pricing-bahrain

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt

## Usage
The main script to run the project is located in main.py. This script reads the raw data, cleans it, handles duplicates, and outputs the final dataset.

Running the Project
Prepare the dataset:

Ensure the raw data files are placed in the Raw_data folder.

Run the analysis:

Execute the following command to start the cleaning and analysis process:

   ```bash
  python main.py
```
3. The cleaned data will be saved in the Cleaned_data folder as output.csv.

Handling Duplicates
The deduplication.py file handles the detection and removal of potential duplicate rows based on several criteria such as price, size, and location. During the execution of the main script, you will be prompted to confirm whether to display, remove, or retain duplicates.

Project Workflow
The analysis proceeds in several stages:

Data Preprocessing:

Raw data is read and cleaned (e.g., handling missing prices, sizes, etc.).

Calculations for missing price per foot values are performed.

Duplicate Handling:

Potential duplicates are identified based on key columns.

Users can choose whether to display, remove, or keep the duplicates.

Data Output:

The cleaned and processed data is saved into a CSV file for further analysis or reporting.

Statistical Analysis
The main statistical focus of the project is to understand how price per foot correlates with various factors like location, classification, and number of roads. Advanced statistical techniques such as regression analysis can be applied to identify trends and correlations.

Contributing
If you would like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
University of Bahrain for supporting the project.

Data sources: Property Finder and Bahrain Finder.
