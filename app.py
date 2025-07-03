# import pandas as pd
# import numpy as np
# import joblib
# import pickle
# import streamlit as st

# model = joblib.load("pollution_model.pkl")
# model_cols = joblib.load("model_columns.pkl")

# st.title("Water Quality Prediction")
# st.write("Predict water pollutants based on year and station id")

# year_input = st.number_input("Enter year", min_value=2000,max_value=2100,value=2022)
# station_id = st.text_input("Enter station id",value='1')

# if st.button('Predict'):
#     if not station_id:
#         st.warning("Please enter station id")
#     else:
#         input_df = pd.DataFrame({'year':[year_input],'id':[station_id]})
#         input_encoded = pd.get_dummies(input_df,columns=['id'])


#         for col in model_cols:
#             if col not in input_encoded.columns:
#                 input_encoded[col] = 0
            
#         input_encoded = input_encoded[model_cols]

#         predicted_pollutants = model.predict(input_encoded)[0]
#         pollutants = ['O2','NO3','NO2','SO4','PO4','Cl']

#         st.subheader(f"Predicted Values for {station_id} in the year {year_input}")

#         predicted_values = {}
#         for p, val in zip(pollutants,predicted_pollutants):
#             st.write(f'{p}:{val:.2f}')


import pandas as pd
import numpy as np
import joblib
import streamlit as st
import matplotlib.pyplot as plt

# Load model and feature columns
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

# Define pollutant names and safety limits
pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'Cl']
safe_limits = {
    'O2': (">=", 5.0, "Low dissolved oxygen"),
    'NO3': ("<=", 50.0, "Nitrate contamination"),
    'NO2': ("<=", 3.0, "Nitrite contamination"),
    'SO4': ("<=", 250.0, "High sulfate"),
    'PO4': ("<=", 5.0, "High phosphate"),
    'Cl': ("<=", 250.0, "High chloride")
}

# Streamlit UI
st.title("💧 Water Quality Prediction")
st.write("Predict water pollutants based on year and station ID, and check water safety.")

# Input fields
year_input = st.number_input("Enter year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("Enter station ID", value='1')

if st.button('Predict'):
    if not station_id:
        st.warning("Please enter station ID")
    else:
        # Input encoding
        input_df = pd.DataFrame({'year': [year_input], 'id': [station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        # Add missing dummy columns
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]  # reorder

        # Predict
        predicted_pollutants = model.predict(input_encoded)[0]

        # Display values
        st.subheader(f"📊 Predicted Pollutant Values for Station {station_id} in {year_input}")
        predicted_values = dict(zip(pollutants, predicted_pollutants))

        # Safety check
        is_safe = True
        bar_colors = []

        for p, val in predicted_values.items():
            op, limit, _ = safe_limits[p]
            if (op == "<=" and val > limit) or (op == ">=" and val < limit):
                is_safe = False
                bar_colors.append("red")
            else:
                bar_colors.append("green")
            st.write(f"**{p}**: {val:.2f} mg/L")

        # Verdict
        st.markdown("---")
        if is_safe:
            st.success("✅ Water is SAFE for drinking")
        else:
            st.error("❌ Water is UNSAFE for drinking")

        # Bar chart
        fig, ax = plt.subplots()
        ax.bar(predicted_values.keys(), predicted_values.values(), color=bar_colors)
        ax.set_ylabel("Concentration (mg/L)")
        ax.set_title("Pollutant Levels")
        st.pyplot(fig)
