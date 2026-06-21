# 🎓 Student Stress Prediction System

A Machine Learning web application that predicts whether a student is likely to be **Stressed** or **Relaxed** based on lifestyle, academic, and personal factors. The application is powered by a **K-Nearest Neighbors (KNN) Classifier** and deployed on **Streamlit Community Cloud**.

## 🌐 Live Demo

🚀 **Try the application here:**

https://students-stress-prediction.streamlit.app/

---

## 📌 Project Overview

Student stress can be influenced by various factors such as sleep patterns, study habits, social media usage, attendance, exam pressure, and family support. This project leverages Machine Learning to analyze these factors and provide a stress prediction in real time.

The application allows users to enter their details through an intuitive web interface and instantly receive a prediction.

---

## ✨ Features

- Interactive Streamlit Web Application
- Real-Time Stress Prediction
- Simple and User-Friendly Interface
- Machine Learning-Based Classification
- Deployed on Streamlit Community Cloud
- Supports Multiple Student Categories

---

## 📊 Dataset

This project uses the **Student Lifestyle and Stress Prediction Dataset** available on Kaggle.

🔗 Dataset:
https://www.kaggle.com/datasets/sridevilavanyacse/student-lifestyle-and-stress-prediction-dataset

### Features Used

| Feature | Description |
|----------|------------|
| Student_Type | School, College, Working Student |
| Sleep_Hours | Average sleep duration per day |
| Study_Hours | Average study hours per day |
| Social_Media_Hours | Daily social media usage |
| Attendance | Attendance percentage |
| Exam_Pressure | Exam pressure level (1–10) |
| Family_Support | Family support level (1–10) |
| Month | Month of the year |

### Target Variable

- **0 → Stressed**
- **1 → Relaxed**

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Joblib

---

## 🤖 Machine Learning Model

### Algorithm

**K-Nearest Neighbors (KNN) Classifier**

The model was trained using lifestyle and academic factors from the dataset and serialized using Joblib for deployment.

### Model File

```text
knn_cls.pkl
```

---

## 📂 Project Structure

```text
StudentStressPrediction/
│
├── app.py
├── knn_cls.pkl
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## ⚙️ Installation and Local Setup

### Clone the Repository

```bash
git clone https://github.com/your-github-username/student-stress-prediction.git

cd student-stress-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```txt
streamlit
numpy
pandas
joblib
scikit-learn
```

---

## 🖥️ How to Use

1. Select the Student Type.
2. Enter Sleep Hours.
3. Enter Study Hours.
4. Enter Social Media Usage Hours.
5. Enter Attendance Percentage.
6. Select Exam Pressure Level.
7. Select Family Support Level.
8. Select Month.
9. Click **Predict**.
10. View the prediction result.

---

## 📸 Application Preview

### Input Parameters

- Student Type
- Sleep Hours
- Study Hours
- Social Media Hours
- Attendance
- Exam Pressure
- Family Support
- Month

### Prediction Result

✅ You are relaxed!

or

❌ You are stressed!

---

## 🚀 Deployment

This application is deployed using **Streamlit Community Cloud**.

🔗 Live Application:
https://students-stress-prediction.streamlit.app/

---

## 🔮 Future Enhancements

- Stress Probability Score
- Model Performance Dashboard
- Multiple Model Comparison
- Data Visualization and Insights
- Personalized Recommendations for Stress Management
- User Authentication and Prediction History

---

## 👨‍💻 Author

**Pyarasani Srinivas**

- B.Tech Computer Science Engineering
- Certified Pega System Architect (CSA)
- Data Analytics & Machine Learning Enthusiast

### Connect with Me

- GitHub: https://github.com/PYARASANISRINIVAS
- LinkedIn: https://www.linkedin.com/in/pya-srinivas/

---

## ⭐ If you like this project

Please consider giving this repository a **Star ⭐** on GitHub to support the project and encourage future improvements.

---

## 📜 License

This project is intended for educational, learning, and portfolio purposes.

Dataset ownership and licensing belong to the original Kaggle dataset creator.
