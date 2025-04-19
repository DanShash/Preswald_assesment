# 🌍 Global Happiness & Economy Explorer

This interactive dashboard visualizes the relationship between economic indicators (like inflation and GDP) and happiness scores across 148 countries from 2015 to 2023.

Built using **Preswald**, the app combines UI widgets, real-world data filtering, and visualizations to help explore how economic conditions shape global well-being.

---

## 📊 Dataset

The dataset merges information from the **World Happiness Index**, **Gallup World Poll**, and **World Bank** covering:

- Happiness Score & Rank
- GDP per Capita
- Various Inflation Metrics:
  - Headline Consumer Price Inflation
  - Energy & Food Inflation
  - Core & Producer Price Inflation
- Social Indicators:
  - Freedom to make life choices
  - Social support
  - Generosity
  - Perceptions of corruption
- Geographical information (Country, Region, Year)

🗂️ File: `data/WHI_Inflation.csv`  
📄 Format: CSV, 2015–2023

---

## 🚀 Features

- 📅 Year and Region selectors
- 😊 Minimum Happiness Score filter (slider)
- 📈 Dynamic scatter plot (GDP vs Happiness Score)
  - Bubble size reflects inflation metric
- 📋 Filtered data table (row limit slider)
- 🧠 Debugging helpers for preview/testing in Preswald
- 🎨 Custom branding (logo, theme color, favicon)

---

## 🛠️ Tech Stack

- **Preswald SDK** (Python-based UI app platform)
- **Plotly Express** for visualizations
- **pandas** for data manipulation
- **Preswald widgets**: `slider`, `selectbox`, `sidebar`, `table`, `text`, `plotly`

---

## 🧪 How to Run in Preswald

> _Note: This project may exceed container startup time during deployment. Use Preview Mode for full experience._

1. Create a new project at [https://app.preswald.com](https://app.preswald.com)
2. Upload:
   - `hello.py` to the **Script** section
   - `WHI_Inflation.csv` to the **data/** folder
   - `Happy_logo.png` and `favicon.ico` to the **images/** folder
   - Paste the contents of `preswald.toml` into the **Config** section
3. Click **Preview** to interact with the dashboard

---

## ⚠️ Deployment Note(I had an issue deploying the project on the platform, thats why I'm uploading it on the Github)

Due to cloud deployment timeouts, the dashboard may fail to deploy if:
- The dataset is large
- The initial chart rendering is slow
- The container does not respond quickly enough

This repo is intended to demonstrate the full functionality and design of the dashboard in Preview Mode.

---

## 📷 Screenshots

I will add 4 screenshots of how did my assesment project looked on the Preview section in Preswal platform.


---

## 🙋‍♂️ Author

Daniels Shashkovs  
Aspiring Machine Learning Engineer & Data Scientist  
[LinkedIn](https://www.linkedin.com/in/dan-shash/)

