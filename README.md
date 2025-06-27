# 💧 WaterQualityPrediction

## 📝 Overview
This project uses **machine learning** to predict water pollutant levels for monitoring stations based on historical data and evaluates whether the water is **safe for drinking** based on predefined safety thresholds (WHO/BIS standards). It also includes **visualizations** to support analysis and reporting.

---

## 📌 Features

- 🔬 **Predicts levels of key pollutants:**
  - Dissolved Oxygen (O₂)
  - Nitrate (NO₃)
  - Nitrite (NO₂)
  - Sulfate (SO₄)
  - Phosphate (PO₄)
  - Chloride (Cl⁻)

- 🧠 Uses a trained regression model (**Random Forest**).

- 🚦 Classifies water as **SAFE** or **UNSAFE** for drinking.

- 📊 Visualizes predicted data using:
  - Bar charts

---

## 🧬 Model Input & Prediction

- **Input**: `station_id`, `year` (dataset already loaded)
- **Model**: Predicts pollutant levels for the given station and year.
- **Output**: Predicted pollutant concentrations in **mg/L**.

### 🔍 Example Output:
Predicted pollutant levels for station '22' in 2024:

O2: 12.60
NO3: 6.90
NO2: 0.13
SO4: 143.08
PO4: 0.50
CL: 67.33


### 💡 Water Quality Analysis — Station 22 (2024)

O2: 12.60 mg/L ✅
NO3: 6.90 mg/L ✅
NO2: 0.13 mg/L ✅
SO4: 143.08 mg/L ✅
PO4: 0.50 mg/L ✅
CL: 67.33 mg/L ✅

✅ Final Verdict: SAFE for drinking
