import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # app/
PROJECT_ROOT = os.path.dirname(BASE_DIR)                # project root

DATA_PATH = os.path.join(PROJECT_ROOT, "data", "your_file_name.csv")
MODEL_PATH = os.path.join(PROJECT_ROOT, "src", "model.pkl")

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

# --- PATH SETUP ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

DATA_PATH = os.path.join(PROJECT_ROOT, "data", "Superstore Sales Performance Analysis (Excel Project).csv")
MODEL_PATH = os.path.join(PROJECT_ROOT, "src", "model.pkl")

# --- LOAD DATA & MODEL ---
df = pd.read_csv(DATA_PATH)
# --- CLEAN NUMERIC COLUMNS ---
cols = ["Store_Sales", "Store_Area", "Items_Available", "Daily_Customer_Count"]

for col in cols:
    df[col] = df[col].replace(r"[^\d.]", "", regex=True)  # remove commas, symbols
    df[col] = pd.to_numeric(df[col], errors="coerce")

# drop bad rows
df.dropna(inplace=True)
model = pickle.load(open(MODEL_PATH, "rb"))

# --- FEATURE ENGINEERING (same logic as notebook) ---
df["sales_per_customer"] = df["Store_Sales"] / df["Daily_Customer_Count"]
df["sales_per_area"] = df["Store_Sales"] / df["Store_Area"]
df["sales_per_item"] = df["Store_Sales"] / df["Items_Available"]

# --- DIAGNOSIS LOGIC ---
def diagnose(row, df):
    if row["Daily_Customer_Count"] > df["Daily_Customer_Count"].median() and row["sales_per_customer"] < df["sales_per_customer"].median():
        return "Low Conversion (traffic not converting)"

    elif row["Store_Area"] > df["Store_Area"].median() and row["sales_per_area"] < df["sales_per_area"].median():
        return "Poor Space Utilization"

    elif row["Items_Available"] > df["Items_Available"].median() and row["sales_per_item"] < df["sales_per_item"].median():
        return "Weak Product Mix"

    else:
        return "No major issue"
    
    # --- RECOMMENDATION FUNCTION ---
def recommend(diagnosis):
    if diagnosis == "Low Conversion (traffic not converting)":
        return "Improve in-store experience, pricing strategy, or promotions"

    elif diagnosis == "Poor Space Utilization":
        return "Optimize store layout or reduce unused floor space"

    elif diagnosis == "Weak Product Mix":
        return "Review product assortment and remove low-performing items"

    else:
        return "Maintain current strategy"

# --- PREDICTION ---
features = ["Store_Area", "Items_Available", "Daily_Customer_Count"]
df["predicted_sales"] = model.predict(df[features])
df["performance_gap"] = df["Store_Sales"] - df["predicted_sales"]
df["diagnosis"] = df.apply(lambda row: diagnose(row, df), axis=1)
df["recommendation"] = df["diagnosis"].apply(recommend)

# --- APP UI ---
st.title("Retail Performance Intelligence Dashboard")

# KPI
under_rate = (df["performance_gap"] < 0).mean() * 100
st.metric("Underperforming Stores (%)", f"{under_rate:.2f}%")

# --- TOP UNDERPERFORMERS ---
st.subheader("Top 10 Underperforming Stores")
worst = df.sort_values("performance_gap").head(10)
st.dataframe(
    worst.reset_index()[[
        "index",
        "Store_Sales",
        "predicted_sales",
        "performance_gap",
        "diagnosis",
        "recommendation"
    ]].rename(columns={"index": "Store_ID"})
)

st.subheader("Performance Summary")

under = df[df["performance_gap"] < 0]
over = df[df["performance_gap"] >= 0]

st.write(f"Underperforming Stores: {len(under)}")
st.write(f"Overperforming Stores: {len(over)}")
# --- PERFORMANCE DISTRIBUTION ---
st.subheader("Performance Gap Distribution")

fig, ax = plt.subplots()
ax.hist(df["performance_gap"], bins=30)
ax.axvline(0)
st.pyplot(fig)

# --- INTERACTIVE PREDICTION ---
st.subheader("Test a Store")

area = st.number_input("Store Area", min_value=0.0)
items = st.number_input("Items Available", min_value=0.0)
customers = st.number_input("Daily Customer Count", min_value=0.0)

if st.button("Predict"):
    input_data = np.array([[area, items, customers]])
    pred = model.predict(input_data)[0]

    st.write("Predicted Sales:", pred)

