# Sonam-ANN-case-study

## 🚀 Overview

Customer churn is one of the biggest challenges for subscription-based businesses. This project builds a **machine learning model** to predict whether a customer is likely to leave (churn) based on their demographics, account details, and service usage.

The project includes:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Model training using Random Forest
* Model evaluation
* Deployment-ready structure (Streamlit app)

---

## 📁 Project Structure

```
customer-churn-prediction/
│
├── data/
│   └── churn_data.csv
│
├── notebooks/
│   └── model.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── predict.py
│
├── app/
│   └── app.py
│
├── model.pkl
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Description

The dataset contains customer information such as:

| Feature         | Description                      |
| --------------- | -------------------------------- |
| CustomerID      | Unique customer ID               |
| Gender          | Male/Female                      |
| Age             | Customer age                     |
| TenureMonths    | Duration of subscription         |
| ContractType    | Monthly / Yearly                 |
| MonthlyCharges  | Monthly bill amount              |
| TotalCharges    | Total amount spent               |
| InternetService | Fiber / DSL / None               |
| SupportTickets  | Number of support tickets raised |
| PaymentMethod   | Payment type                     |
| Churn           | Target variable (Yes/No)         |

---

## 🔍 Exploratory Data Analysis

Key insights:

* Customers with **monthly contracts** churn more
* Higher **monthly charges** correlate with churn
* Customers with more **support tickets** are more likely to churn
* **Fiber users** show higher churn compared to DSL

---

## 🤖 Model Building

### Algorithm Used:

* Random Forest Classifier

### Steps:

1. Data cleaning (removed `CustomerID`)
2. Encoding categorical variables
3. Train-test split
4. Model training
5. Evaluation

---

## 📈 Model Evaluation

Metrics used:

* Accuracy Score
* Confusion Matrix
* Classification Report

---

## 💾 Model Saving

The trained model is saved as:

```
model.pkl
```

---

## 🖥️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train the model

```
cd src
python train_model.py
```

### 4️⃣ Run Jupyter Notebook (optional)

```
cd notebooks
jupyter notebook model.ipynb
```

### 5️⃣ Run Streamlit App

```
cd app
streamlit run app.py
```

---

## 🌐 Deployment

You can deploy this project using:

* Streamlit Community Cloud
* Render
* Railway

---

## 📌 Future Improvements

* Use advanced models like XGBoost
* Hyperparameter tuning
* Handle class imbalance
* Add feature engineering
* Deploy REST API using Flask/FastAPI
* Improve UI with better dashboard

---

## 🧠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit

---

## 🙌 Conclusion

This project demonstrates an end-to-end machine learning workflow:
from data preprocessing to deployment. It can help businesses proactively identify customers at risk of churning and take action to retain them.

---

## 📬 Contact

If you have any questions or suggestions, feel free to connect!
