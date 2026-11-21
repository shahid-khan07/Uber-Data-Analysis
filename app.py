
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Uber Data Analysis Dashboard",
    page_icon="🚕",
    layout="wide"
)

# Dashboard title
st.title("🚕 Uber NYC Pickup Analytics")
st.markdown(
    "### April 2014 | Interactive Data Analysis Dashboard"
)

st.markdown(
    "Explore pickup trends, popular locations, "
    "daily activity and Uber base performance."
)

st.divider()

# Load cleaned dataset
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "cleaned" / "uber_cleaned.csv"
df = pd.read_csv(DATA_PATH)

# Load dataset
df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])


# Date Range Filter
st.sidebar.header("Dashboard Filters")

min_date = df["date"].min().date()
max_date = df["date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(selected_dates) == 2:
    start_date, end_date = selected_dates

    df = df[
        (df["date"].dt.date >= start_date) &
        (df["date"].dt.date <= end_date)
    ]

# Uber Base Filter
base_options = ["All Bases"] + sorted(df["Base"].unique().tolist())

selected_base = st.sidebar.selectbox(
    "Select Uber Base",
    base_options
)

if selected_base != "All Bases":
    df = df[df["Base"] == selected_base]

# KPI metrics
total_pickups = len(df)
total_bases = df["Base"].nunique()
total_days = df["day"].nunique()
busiest_hour = df["hour"].value_counts().idxmax()

# Display KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Pickups", f"{total_pickups:,}")
col2.metric("Uber Bases", total_bases)
col3.metric("Days Analyzed", total_days)
col4.metric("Busiest Hour", f"{busiest_hour}:00")


# Pickup Summary
st.header("📊 Pickup Summary")

summary_col1, summary_col2, summary_col3 = st.columns(3)

summary_col1.metric(
    "Average Pickups per Hour",
    f"{len(df) / 24:,.0f}"
)

summary_col2.metric(
    "Average Pickups per Day",
    f"{len(df) / max(df['date'].nunique(), 1):,.0f}"
)

summary_col3.metric(
    "Unique Pickup Locations",
    df.groupby(["Lat_Rounded", "Lon_Rounded"]).ngroups
)

# Dataset preview
st.header("Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)


# Hourly Pickup Analysis
st.header("Hourly Pickup Analysis")

hourly_pickups = df["hour"].value_counts().sort_index()

st.bar_chart(hourly_pickups)


# Average Pickups by Weekday
st.header("Average Pickups by Weekday")

daily_summary = (
    df.groupby(["date", "day_name"])
    .size()
    .reset_index(name="Pickups")
)

weekday_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

average_weekday = (
    daily_summary.groupby("day_name")["Pickups"]
    .mean()
    .reindex(weekday_order)
)

st.bar_chart(average_weekday)


# Daily Pickup Trends
st.header("Daily Pickup Trends - April 2014")

daily_pickups = df.groupby("day").size().sort_index()

st.line_chart(daily_pickups)


# Uber Pickups by Base
st.header("Uber Pickups by Base")

base_pickups = df["Base"].value_counts().sort_values(ascending=False)

st.bar_chart(base_pickups)


# Top 10 Pickup Locations
st.header("Top 10 Uber Pickup Locations")

top_locations = (
    df.groupby(["Lat_Rounded", "Lon_Rounded"])
    .size()
    .reset_index(name="Total_Pickups")
    .sort_values("Total_Pickups", ascending=False)
    .head(10)
)

top_locations["Location"] = (
    top_locations["Lat_Rounded"].astype(str)
    + ", "
    + top_locations["Lon_Rounded"].astype(str)
)

st.bar_chart(
    top_locations.set_index("Location")["Total_Pickups"]
)


# Geographic Distribution of Pickups
st.header("Geographic Distribution of Uber Pickups")

st.map(
    df.rename(columns={"Lat": "latitude", "Lon": "longitude"})[
        ["latitude", "longitude"]
    ],
    latitude="latitude",
    longitude="longitude"
)



# Download Filtered Dataset
st.header("📥 Download Data")

csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Dataset",
    data=csv_data,
    file_name="uber_filtered_data.csv",
    mime="text/csv"
)


# Dashboard Footer
st.divider()

st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <p>Uber NYC Pickup Analytics | April 2014</p>
        <p>Built with Python, Pandas and Streamlit</p>
        <p>Data Analytics Portfolio Project</p>
    </div>
    """,
    unsafe_allow_html=True
)
