
import pandas as pd
import os

# Load raw dataset
input_path = "data/raw/uber-raw-data-apr14.csv"
df = pd.read_csv(input_path)

print("Original records:", len(df))

# Convert Date/Time to datetime
df["Date/Time"] = pd.to_datetime(df["Date/Time"])

# Remove exact duplicate records
df_cleaned = df.drop_duplicates(
    subset=["Date/Time", "Lat", "Lon", "Base"]
).copy()

# Create time-based features
df_cleaned["hour"] = df_cleaned["Date/Time"].dt.hour
df_cleaned["day_name"] = df_cleaned["Date/Time"].dt.day_name()
df_cleaned["day"] = df_cleaned["Date/Time"].dt.day
df_cleaned["date"] = df_cleaned["Date/Time"].dt.date

# Round coordinates
df_cleaned["Lat_Rounded"] = df_cleaned["Lat"].round(2)
df_cleaned["Lon_Rounded"] = df_cleaned["Lon"].round(2)

# Save cleaned dataset
os.makedirs("data/cleaned", exist_ok=True)

df_cleaned.to_csv(
    "data/cleaned/uber_cleaned.csv",
    index=False
)

print("Cleaned records:", len(df_cleaned))
print("Removed duplicates:", len(df) - len(df_cleaned))
print("Cleaned dataset saved successfully!")
