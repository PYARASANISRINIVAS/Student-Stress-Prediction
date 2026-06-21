# 🎓 Student Stress Prediction System

A Machine Learning web application that predicts whether a student is likely to be **Stressed** or **Relaxed** based on lifestyle, academic, and personal factors. The application is powered by a **K-Nearest Neighbors (KNN) Classifier**, achieving **80% prediction accuracy**, and is deployed on **Streamlit Community Cloud**.

## 🌐 Live Demo

🚀 **Try the application here:**

https://students-stress-prediction.streamlit.app/

---

## 📌 Project Overview

Student stress is influenced by various lifestyle and academic factors such as sleep patterns, study habits, social media usage, attendance, exam pressure, and family support. This project leverages Machine Learning to analyze these factors and predict whether a student is likely to be stressed or relaxed.

The application provides an interactive interface where users can enter their details and receive an instant prediction powered by a trained KNN classification model.

---

## ✨ Features

- Interactive Streamlit Web Application
- Real-Time Stress Prediction
- User-Friendly Interface
- Machine Learning-Based Classification
- Deployed on Streamlit Community Cloud
- Supports Multiple Student Categories
- Instant Prediction Results

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

| Value | Meaning |
|---------|---------|
| 0 | Stressed |
| 1 | Relaxed |

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

The KNN classifier was trained using student lifestyle and academic data to classify stress levels. The trained model was serialized using Joblib and integrated into the Streamlit application for real-time predictions.

### Model File

```text
knn_cls.pkl
```

---

## 📈 Model Performance

The trained KNN model was evaluated using a test dataset and achieved the following results.

### Overall Accuracy

| Metric | Score |
|----------|----------|
| Accuracy | **80%** |

### Classification Report

| Class | Precision | Recall | F1-Score |
|---------|---------|---------|---------|
| Stressed (0) | 0.83 | 0.89 | 0.86 |
| Relaxed (1) | 0.70 | 0.58 | 0.63 |

### Performance Summary

- ✅ Overall Accuracy: **80%**
- ✅ Strong performance in identifying stressed students
- ✅ Good precision and recall for stress detection
- ✅ Suitable for educational and portfolio demonstration purposes

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
git clone https://github.com/PYARASANISRINIVAS/student-stress-prediction.git

cd student-stress-prediction
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

The application will run locally at:

```text
http://localhost:8501
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

### Prediction Output

#### Relaxed Student

```text
✅ You are relaxed!
```

#### Stressed Student

```text
❌ You are stressed!
```

> Add screenshots of your deployed application here to make the repository more attractive and professional.

---

## 🚀 Deployment

The application is deployed using **Streamlit Community Cloud** and can be accessed online without any installation.

🔗 Live Application:

https://students-stress-prediction.streamlit.app/

---

## 🔮 Future Enhancements

- Stress Probability Score
- Multiple Model Comparison
- Model Performance Dashboard
- Feature Importance Visualization
- Personalized Stress Management Suggestions
- User Authentication
- Prediction History Tracking
- Advanced Analytics Dashboard

---

## 👨‍💻 Author

### Pyarasani Srinivas

### Connect With Me

🔗 GitHub

https://github.com/PYARASANISRINIVAS

🔗 LinkedIn

https://www.linkedin.com/in/pya-srinivas/

---

## ⭐ Support

If you found this project useful, please consider giving it a **Star ⭐** on GitHub.

Contributions, suggestions, and feedback are always welcome.

---

## 📜 License

This project is intended for educational, learning, and portfolio purposes.

The dataset belongs to its original creator on Kaggle and is used solely for academic and demonstration purposes.
