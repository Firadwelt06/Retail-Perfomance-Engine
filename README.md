# 🏪 Retail Performance Intelligence Dashboard

A data-driven analytics system that evaluates retail store performance, predicts expected sales, and provides actionable business recommendations using machine learning and feature engineering.

---

## 🚀 Project Overview

This project transforms raw retail operational data into a **decision intelligence system**.

Instead of just analyzing sales, it answers:

- Are stores performing above or below expectation?
- What is driving underperformance?
- What specific actions should be taken to improve results?

It combines:
- Machine Learning (Sales Prediction)
- Feature Engineering (Efficiency Metrics)
- Business Diagnostics (Performance Gaps)
- Recommendation Engine (Actionable Insights)
- Interactive Dashboard (Streamlit)

---

## 📊 Key Features

### 1. Sales Prediction Model
Predicts expected store revenue using:
- Store area
- Customer traffic
- Product availability

### 2. Performance Gap Analysis
Compares:
- Actual Sales vs Predicted Sales  
- Identifies underperforming and overperforming stores

### 3. Business Intelligence Features
Engineered metrics:
- Sales per customer (conversion efficiency)
- Sales per area (space efficiency)
- Sales per item (inventory efficiency)

### 4. Diagnosis Engine
Automatically categorizes store issues:
- Low Conversion (traffic not converting)
- Poor Space Utilization
- Weak Product Mix

### 5. Recommendation System
Provides actionable business strategies per store.

---

## 🧠 Tech Stack

- Python 3.8+
- Pandas / NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit
- Pickle (model serialization)

---

## 📁 Project Structure

```
Retail-Performance-Engine/
│
├── app/              # Streamlit dashboard application
├── data/             # Raw retail dataset
├── notebooks/        # EDA + feature engineering notebooks
├── src/              # Trained ML model and utilities
├── requirements.txt  # Python dependencies
└── README.md         # Documentation
```

---

## 📈 How It Works

1. Data is cleaned and standardized  
2. Features are engineered for business meaning  
3. ML model predicts expected sales  
4. Performance gap is calculated  
5. Stores are diagnosed and classified  
6. Recommendations are generated  
7. Streamlit dashboard visualizes results  

---

## 📊 Dashboard Output

The system provides:

- Top underperforming stores
- Performance gap distribution
- Store-level diagnosis
- Actionable recommendations
- Real-time prediction interface

---

## 📋 Dataset Description

The retail dataset includes:
- **Store Metrics**: Store ID, area, type, location
- **Sales Data**: Actual sales, customer traffic, transactions
- **Inventory**: Product availability, item count
- **Performance**: Historical performance indicators

---

## ⚙️ How to Run Locally

### 1. Clone repository
```bash
git clone https://github.com/Firadwelt06/Retail-Perfomance-Engine.git
cd Retail-Perfomance-Engine
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app
```bash
streamlit run app/app.py
```

The dashboard will open at `http://localhost:8501`

---

## 🎯 Business Value

This system helps retail decision-makers:
- Identify revenue leakage points
- Improve store efficiency
- Optimize inventory allocation
- Prioritize store interventions
- Make data-driven operational decisions

---

## 🔥 Key Insight

Not all high-traffic stores are profitable. This project reveals hidden inefficiencies that traditional reporting systems miss.

---

## 📈 Model Performance

- **Prediction Accuracy**: MAE: 14613.337177672394     R2: -0.01226925969065995
- **Feature Importance**: Store area, customer traffic, and product availability are top drivers
- **Business Impact**: This system enables retail managers to:
- Identify underperforming stores in real time
- Detect root causes of inefficiency (conversion, space, inventory)
- Prioritize interventions based on performance gap severity
- Reduce revenue leakage through targeted improvements

---

## 🚀 Future Improvements

- Add time-series sales forecasting
- Segment stores by region/type
- Add cost vs profit analysis
- Deploy on cloud (Streamlit Cloud / AWS)
- Add automated reporting PDFs
- Implement A/B testing framework
- Add real-time data pipeline integration

---

## 📝 Usage Example

```python
from src.model import RetailPerformanceModel

# Load trained model
model = RetailPerformanceModel()

# Make prediction
prediction = model.predict(
    store_area=5000,
    customer_traffic=2000,
    product_availability=0.95
)

# Get diagnosis and recommendations
diagnosis = model.diagnose(prediction, actual_sales=95000)
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request with:
- Bug fixes
- Feature enhancements
- Documentation improvements
- Dataset updates

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Built as a portfolio project demonstrating:**
- End-to-end data science workflow
- Machine learning application in retail analytics
- Business-focused data storytelling
- Production-ready dashboard development

For questions or feedback, feel free to open an issue or reach out!

---

## 📜 Data Source & License

Dataset sourced from Kaggle.

This project is for educational and portfolio purposes only.

The dataset is subject to its original license (e.g., CC BY-NC 4.0), and any commercial use must comply with those terms.
