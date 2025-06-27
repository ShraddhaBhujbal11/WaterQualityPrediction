# WaterQualityPrediction
OVERVIEW
This project uses machine learning to predict water pollutant levels for monitoring stations based on historical data and evaluates whether the water is safe for drinking based on predefined safety thresholds. It also provides data visualization to support analysis.

---
📌 FEATURES
Predicts levels of key pollutants:

Dissolved Oxygen (O₂)

Nitrate (NO₃)

Nitrite (NO₂)

Sulfate (SO₄)

Phosphate (PO₄)

Chloride (Cl⁻)


Uses a trained regression model (Random Forest).

Classifies water as SAFE or UNSAFE based on WHO/BIS standards.

Visualizes predicted data using -> Bar charts

---
🧬 MODEL INPUT AND PREDICTION 
Input: station_id, year  [Dataset already loaded]

Model: Predicts pollutant levels for given station and year.

Output: Numerical values for each pollutant (in mg/L).

Example:- Predicted pollutant levels for station '22' in 2024:
  O2: 12.60
  NO3: 6.90
  NO2: 0.13
  SO4: 143.08
  PO4: 0.50
  CL: 67.33


  *** Water Quality Analysis — Station 22 (2024) ***

O2: 12.60 mg/L ->
NO3: 6.90 mg/L ->
NO2: 0.13 mg/L ->
SO4: 143.08 mg/L ->
PO4: 0.50 mg/L ->
CL: 67.33 mg/L ->

 [Final Verdict: SAFE for drinking]
