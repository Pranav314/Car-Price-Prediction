# 🚗 Car Price Prediction

A machine learning project that predicts the **selling price of a used car** based on key features such as purchase year, purchase price, kilometers driven, fuel type, seller type, transmission, and number of previous owners.  
Includes a **desktop GUI application (wxPython)** for easy and interactive predictions.

---

## 📌 Features

- Predicts estimated selling price of a car  
- Clean and user-friendly GUI  
- Easy to run, no ML expertise required  
- Uses regression algorithms for accurate predictions  
- Loads trained model from a `.pkl` file  

---

## 🧠 Machine Learning Overview

- **Data Preprocessing:** cleaning, encoding, feature selection  
- **Model Training:** Linear Regression, Lasso Regression  
- **Model Evaluation:** R² score, actual vs predicted comparison  
- **Model Saving:** final model stored as `car_price_model.pkl`  

---

## 🖥 GUI Application (wxPython)

### **User Inputs**
- Year you bought the car  
- Price you bought the car for (in lakh)  
- Total kilometers driven  
- Fuel type (Petrol / Diesel / CNG)  
- Seller type (Dealer / Individual)  
- Transmission (Manual / Automatic)  
- Number of previous owners  

### **Output**
- **Predicted Selling Price (in lakh)**

---

## 📂 Project Structure

```
Car-Price-Prediction/
│
├── car_price_model.pkl        # Trained ML model
├── gui.py                     # GUI application
├── model_utils.py             # Model loader
└── Car-Price-Prediction.ipynb # Notebook used for ML training
```

---

## 🚀 How to Run

### **1. Install dependencies**
```bash
pip install wxPython numpy scikit-learn
```

### **2. Run GUI**
```bash
python gui.py
```

---

## 📊 Dataset Details

Features included:
- Car Name  
- Year  
- Present Price  
- Selling Price  
- Kms Driven  
- Fuel Type  
- Seller Type  
- Transmission  
- Owner  

Dataset source: **CarDekho Used Car Dataset**

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- wxPython  
- Matplotlib & Seaborn  

---

## 📸 Screenshots  
<img width="511" height="695" alt="image" src="https://github.com/user-attachments/assets/8c9ffcb4-6b57-4233-8d4e-a564f04baf0d" />


---

