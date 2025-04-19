# This code includes embedded debugging features (✅ markers, row counts, column list)
# because the Preswald Preview environment does not provide built-in error logs.
# During development, several silent failures occurred (e.g., in charts and filters),
# so these debug lines helped track where the app was breaking. (I will suggest the core team of Preswald to think about adding such debug features on their platform)

# Additionally, due to limited time and scope, no formal data cleaning or preprocessing
# (e.g., handling missing values, normalizing data, or correcting anomalies) was done.
# As a result, the scatter plot and table visuals may not respond as smoothly or
# intuitively as expected in a fully production-ready data app.
# interactivity based on a real-world dataset (Happiness + Inflation 2015–2023).
# ------------------------------------------------------------
from preswald import text, plotly, connect, get_df, table, slider, selectbox, sidebar
import pandas as pd
import plotly.express as px

# Connect & Sidebar
connect()
sidebar(defaultopen=True)

#App Header
text("# 🌍 Global Happiness vs Economy Dashboard")
text("Explore how economic factors like GDP, inflation, and happiness scores vary across the world from 2015 to 2023.")

# Load dataset
df = get_df("WHI_Inflation")
df.columns = df.columns.str.strip()

#Debug: Confirm dataset loaded
text("✅ Dataset loaded")
text(str(df.columns.tolist()))  # ✅ Debug: Show actual column names

#Year Selector
text("### 📅 Select a Year")
years = sorted([int(year) for year in df["Year"].dropna().unique()])
selected_year = selectbox("Choose a year to analyze", options=years, default=years[-1])

#Region Selector
text("### 🌍 Select a Region")
regions = sorted(df["Continent/Region"].dropna().unique())
selected_region = selectbox("Choose a region to explore", options=regions, default=regions[0])

#Happiness Score Slider
text("### 😊 Filter by Happiness Score")
text("Use the slider below to only show countries above a certain happiness threshold.")
min_score = round(df["Score"].min(), 1)
max_score = round(df["Score"].max(), 1)
threshold = slider("Min Happiness Score", min_val=min_score, max_val=max_score, step=0.1, default=5.0)

#Inflation Metric Selector
text("### 📈 Select Inflation Type for Bubble Size")
text("Choose which type of inflation will determine the bubble sizes in the scatter plot.")
selected_inflation = selectbox(
    label="Choose Inflation Metric",
    options=[
        "Headline Consumer Price Inflation",
        "Energy Consumer Price Inflation",
        "Food Consumer Price Inflation",
        "Official Core Consumer Price Inflation",
        "Producer Price Inflation"
    ],
    default="Headline Consumer Price Inflation"
)

#Apply filtering
filtered_df = df[
    (df["Year"] == selected_year) &
    (df["Continent/Region"] == selected_region) &
    (df["Score"] > threshold)
]

# Debug: Show filtered row count
text(f"✅ Filtered rows: {len(filtered_df)}")

#Filtered Table with Row Limit Slider
if len(filtered_df) == 0:
    text("⚠️ No data matches the current filters. Try adjusting the filters above.")
else:
    text("### 📋 Table of Filtered Countries")
    text("These are the countries that match your selected filters.")

    #Row limit slider
    max_display = min(len(filtered_df), 100)  # Limit max slider range to 100 or row count
    row_limit = slider("Max rows to display", min_val=5, max_val=max_display, step=5, default=min(10, max_display))
    table(filtered_df.head(row_limit), title=f"Top {row_limit} Countries by Filters")

    # Drop NaNs in selected inflation metric to prevent chart crash
    chart_df = filtered_df.dropna(subset=[selected_inflation])

    #Scatter Plot
    text("### 📉 Happiness vs GDP Chart")
    text(f"This chart compares GDP per capita and happiness scores. The bubble size shows **{selected_inflation.lower()}**.")

    fig = px.scatter(
        chart_df,
        x="GDP per Capita",
        y="Score",
        size=selected_inflation,
        color="Country",
        hover_name="Country",
        title=f"Happiness vs GDP ({selected_inflation}) – {selected_region}, {selected_year}"
    )
    plotly(fig)