# ❤️ Heart Disease Prediction System

🚀 An end-to-end Machine Learning project that predicts the likelihood of heart disease using patient health data, with an interactive Streamlit web application.

---

## 📌 Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help in timely intervention and better healthcare decisions.

This project builds a machine learning model to classify whether a patient is at risk of heart disease based on clinical features such as age, cholesterol, blood pressure, etc.

---

## 🎯 Objective

- Predict heart disease risk using machine learning  
- Build a clean and scalable ML pipeline  
- Deploy the model using an interactive Streamlit interface  

---

## 🧠 Model Details

- Model: **Logistic Regression**
- Framework: **Scikit-learn**
- Preprocessing:
  - StandardScaler for feature scaling  
- Evaluation Metric:
  - Accuracy Score  

---

## ⚙️ Workflow

1. Data Loading and Cleaning  
2. Feature Selection  
3. Train-Test Split  
4. Feature Scaling  
5. Model Training  
6. Model Evaluation  
7. Model Saving (`model.pkl`, `scaler.pkl`)  
8. Deployment using Streamlit  

---

## 📊 Results

- Accuracy: **~85%**  
- Model shows good performance on balanced dataset  
- Provides probability-based prediction for better interpretation  

---

## 🧪 Features

- ✅ End-to-end ML pipeline  
- ✅ Separate training and deployment scripts  
- ✅ Interactive user input via Streamlit  
- ✅ Real-time prediction with probability score  
- ✅ Model persistence using `joblib`  

---

## 💻 How It Works

- User inputs medical data through the UI  
- Data is scaled using saved `scaler.pkl`  
- Model (`model.pkl`) predicts risk  
- Output shows:
  - Risk level (High / Low)  
  - Probability score  

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 2️⃣ Train the model (optional)

```bash
python train.py
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```

---

📂 Project Structure

heart-disease-prediction/
│
├── train.py        # Model training script
├── app.py          # Streamlit web app
├── model.pkl       # Trained model
├── scaler.pkl      # Saved scaler
├── heart.csv       # Dataset
├── requirements.txt
├── README.md

---
💡 Key Insights
  * Feature scaling improves model performance
  * Logistic Regression works well for binary classification
  * Separating training and deployment improves efficiency
  * Probability-based output gives better interpretability

---
⚠️ Disclaimer

This application is for educational purposes only and should not be used for medical diagnosis.

---

🚀 Future Improvements
 * Use advanced models (Random Forest, XGBoost)
 * Add ROC-AUC and confusion matrix visualization
 * Deploy using Streamlit Cloud
 * Improve UI/UX design

---

💼 Applications

 * Healthcare risk assessment
 * Clinical decision support
 * Preventive health analysis

---

👨‍💻 Author

Khaja Pasha

GitHub: https://github.com/khajapashas722-alt
