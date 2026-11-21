# Uber NYC Pickup Data Analysis – April 2014

## Project Overview

This project analyzes Uber pickup data from New York City for April 2014 using Python. The objective is to understand pickup patterns by hour, weekday, date, geographic location, and Uber base.

An interactive Streamlit dashboard is also included to explore pickup trends using date and Uber base filters.

## Dataset Information

- **Dataset:** Uber Raw Data – April 2014
- **Original Records:** 564,516
- **Cleaned Records:** 556,767
- **Columns:** Date/Time, Lat, Lon, Base, hour, day_name, day, date, Lat_Rounded, Lon_Rounded

**Dataset availability:** The cleaned CSV file is approximately 43.7 MB and is not included in this GitHub repository. Place the original dataset in `data/raw/` before running the cleaning script.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Streamlit
- Plotly
- VS Code

## Data Cleaning and Preprocessing

- Checked the dataset for missing values.
- Identified 7,749 exact duplicate records based on Date/Time, Lat, Lon, and Base.
- Removed exact duplicates in a separate cleaned dataset.
- Converted Date/Time into datetime format.
- Created time-based features: hour, day_name, day, and date.
- Created rounded latitude and longitude columns for location grouping.
- Saved the cleaned dataset as `uber_cleaned.csv`.

**Note:** The dataset does not contain unique pickup IDs. Therefore, identical records were treated as duplicates for this analysis. This is an assumption, not proof that every repeated record was erroneous.

## Analysis & Visualizations

The project includes six visualizations:

1. Uber pickups by hour.
2. Average pickups by weekday.
3. Daily pickups in April 2014.
4. Geographic distribution of pickup locations.
5. Top 10 pickup locations.
6. Uber pickups by base.

The charts are available in the `visualizations/` folder.

## Key Findings

- 5 PM was the busiest pickup hour in the dataset.
- Pickup activity varied across weekdays.
- Pickup locations were heavily concentrated around Manhattan.
- B02682 recorded the highest number of pickup records among the five bases.

## Interactive Streamlit Dashboard

The project includes an interactive dashboard with:

- Total pickup records and key performance indicators.
- Date range filter.
- Uber base filter.
- Hourly, weekday, and daily pickup trends.
- Pickup distribution by Uber base.
- Top 10 pickup locations.
- Geographic pickup map.
- Filtered dataset download option.

## Project Structure

```text
Uber-Data-Analysis/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── notebooks/
│   └── uber_analysis.ipynb
│
├── screenshots/
│   └── dashboard.pdf
│
├── src/
│   └── data_cleaning.py
│
├── visualizations/
│   ├── 01_hourly_pickups.png
│   ├── 02_average_weekday_pickups.png
│   ├── 03_daily_pickups.png
│   ├── 04_pickup_locations.png
│   ├── 05_top_10_locations.png
│   └── 06_pickups_by_base.png
│
├── requirements.txt
└── README.md
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/shahid-khan07/Uber-Data-Analysis.git
```

### 2. Open the Project Folder

```bash
cd Uber-Data-Analysis
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the Dataset

Place the original CSV file inside:

```text
data/raw/uber-raw-data-apr14.csv
```

### 5. Run the Data Cleaning Script

```bash
python src/data_cleaning.py
```

This generates the cleaned CSV file inside `data/cleaned/`.

### 6. Run the Jupyter Notebook

Open:

```text
notebooks/uber_analysis.ipynb
```

Run the notebook cells in order.

### 7. Launch the Streamlit Dashboard

```bash
python -m streamlit run dashboard/app.py
```

## Limitations

- The dataset contains pickup records only.
- It does not include fares, passenger details, drop-off locations, trip distances, or trip durations.
- The analysis focuses on pickup patterns rather than revenue or trip-performance analysis.
- Duplicate removal is based on exact matching records because unique pickup IDs are unavailable.

## Author

**Shahid Khan**

BCA Student | Aspiring Data Analyst

GitHub: https://github.com/shahid-khan07
