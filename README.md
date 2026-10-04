# FraudHive 🛡️

### AI-Driven Credit Card Fraud Detection System

FraudHive is a machine learning-based credit card fraud detection system that classifies transactions as **Genuine** or **Fraudulent**. The project uses a **Random Forest Classifier** for prediction and integrates the trained model with a **Flask backend** and **React frontend** to provide an end-to-end transaction prediction system.

## 🚀 Features

* Credit card transaction fraud detection
* Random Forest-based classification
* Transaction preprocessing and feature scaling
* Fraud probability prediction
* React-based user interface
* Flask REST API for model communication
* Fraud alerts and prediction results
* Saved ML model and scaler for application integration

## 🧠 Machine Learning

The model is trained using the **Credit Card Fraud Detection Dataset** from Kaggle.

### Model

* **Algorithm:** Random Forest Classifier
* **Number of Trees:** 100
* **Train-Test Split:** 80:20
* **Random State:** 42
* **Stratified Split:** Yes
* **Feature Scaling:** StandardScaler applied to `Time` and `Amount`

### Evaluation Results

| Metric        |       Result |
| ------------- | -----------: |
| Accuracy      |        99.1% |
| Precision     |        93.4% |
| Recall        |        88.1% |
| F1-Score      |        0.907 |
| ROC-AUC       |        0.986 |
| Training Time | 12.8 seconds |

## 🔄 System Workflow

```text
Transaction Input
       ↓
Data Preprocessing
       ↓
Feature Scaling
       ↓
Random Forest Model
       ↓
Fraud / Genuine Prediction
       ↓
Prediction Probability
       ↓
Display Result
```

## 🏗️ Tech Stack

**Machine Learning**

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

**Backend**

* Flask

**Frontend**

* React
* TypeScript

**Development Tools**

* Jupyter Notebook
* VS Code
* Git & GitHub

## 📂 Project Structure

```text
FraudHive/
│
├── dataset/
│   └── creditcard.csv
│
├── model/
│   ├── fraud_model.pkl
│   └── scaler.pkl
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── ...
│
├── notebooks/
│   └── ...
│
├── requirements.txt
└── README.md
```

> The exact folder structure may vary depending on the final project organization.

## 📊 Dataset

**Credit Card Fraud Detection Dataset**
Source: Kaggle

The dataset contains transaction features including `Time`, `V1–V28`, `Amount`, and the target variable `Class`.

* `Class = 0` → Genuine transaction
* `Class = 1` → Fraudulent transaction

The dataset is highly imbalanced, making metrics such as **precision, recall, F1-score, and ROC-AUC** important in addition to accuracy.

## 🖥️ Application

FraudHive provides a web-based interface where users can enter transaction information and receive a prediction from the trained machine learning model.

The application consists of:

**React Frontend → Flask API → ML Model → Prediction → Frontend Result**

The system displays whether the transaction is **Genuine or Fraudulent**, along with the prediction probability.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd FraudHive
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Flask backend

```bash
python app.py
```

### 4. Start the React frontend

Navigate to the frontend directory and run:

```bash
npm install
npm run dev
```

The application can then be accessed through the local development URL provided by the frontend.

## 📈 Future Scope

* Train and evaluate using larger and more diverse datasets
* Hyperparameter tuning and comparison with other ML models
* Real-time transaction monitoring
* Prediction history and reporting
* Improved fraud alert mechanisms
* Cloud/web deployment
* Enhanced security and production-level scalability

## ⚠️ Limitations

FraudHive is an **academic prototype** and is not intended for direct use in real banking systems. Its performance depends on the dataset used for training and may not generalize perfectly to transactions from different banks, regions, or time periods.

## 👥 Project

**FraudHive – AI-driven Credit Card Fraud Detection System**

Developed as part of a **Machine Learning PBL Project**.

**Technologies:** Python • Scikit-learn • Random Forest • Flask • React • TypeScript
