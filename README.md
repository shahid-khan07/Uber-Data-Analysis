# Uber Data Analysis – NYC (April 2014)

## Project Overview
This project analyzes Uber pickup data from New York City for April 2014 using Python. The goal is to explore pickup patterns by hour, weekday, date, geographic location, and Uber base.

## Dataset Information
- **Dataset:** Uber Raw Data – April 2014
- **Original Records:** 564,516
- **Cleaned Records:** 556,767
- **Columns:** Date/Time, Lat, Lon, Base, hour, day_name, day, date, Lat_Rounded, Lon_Rounded

## Tools & Technologies
- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- VS Code

## Data Cleaning
- Checked for missing values.
- Identified 7,749 exact duplicate records based on Date/Time, Lat, Lon, and Base.
- Removed those duplicate records in a separate cleaned dataset.
- Created time-based features for analysis.
- Created rounded coordinates for grouping pickup locations.
- Saved the cleaned dataset as `uber_cleaned.csv`.

**Note:** The dataset does not contain unique pickup IDs, so repeated identical records were treated as duplicates for this analysis. This is an assumption, not proof that every repeated record was erroneous.

## Analysis & Visualizations
The project includes six visualizations:

1. Uber pickups by hour.
2. Average pickups by weekday.
3. Daily pickups in April 2014.
4. Geographic distribution of pickup locations.
5. Top 10 pickup locations.
6. Uber pickups by base.

## Key Findings
- 5 PM was the busiest pickup hour in the dataset.
- Pickup activity varied across weekdays.
- Pickup locations were heavily concentrated around Manhattan.
- B02682 had the highest number of pickup records among the five bases.

## Project Structure
```text
Uber-Data-Analysis/
├── data/
│   ├── raw/
│   └── cleaned/
├── notebooks/
├── src/
├── outputs/
│   ├── charts/
│   └── charts_backup/
├── dashboard/
├── requirements.txt
└── README.md
```

## How to Run
1. Clone or download this repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Open `notebooks/uber_analysis.ipynb` in Jupyter Notebook or VS Code.
4. Run the notebook cells in order.

## Limitations
This dataset contains pickup records only. It does not include fares, passenger details, drop-off locations, trip distances, or trip durations. Therefore, this project focuses on pickup patterns rather than revenue or trip-performance analysis.

## Author
Data Analytics Project Portfolio