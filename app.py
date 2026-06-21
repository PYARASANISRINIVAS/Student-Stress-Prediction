import streamlit as st
import numpy as np
import pandas as pd
import joblib 
import sklearn

st.title("Student Stress Prediction")

model=joblib.load("D:\Data Science\DataScienceProject\StrudentStressClassification\knn_cls.pkl")




student_type = st.selectbox(
    "Student Type",
    ["college", "school","working_student"]
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0,
    step=0.5
)

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

social_media_hours = st.number_input(
    "Social Media Hours",
    min_value=0.0,
    max_value=24.0,
    value=2.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=1.0
)

exam_pressure = st.selectbox(
    "Exam Pressure",
    [1,2,3,4,5,6,7,8,9,10]
)

family_support = st.selectbox(
    "Family Support",
    [1,2,3,4,5,6,7,8,9,10]
)

month = st.selectbox(
    "Month",
    [1,2,3,4,5,6,7,8,9,10,11,12]
)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "Student_Type":[student_type],
        "Sleep_Hours":[sleep_hours],
        "Study_Hours":[study_hours],
        "Social_Media_Hours":[social_media_hours],
        "Attendance":[attendance],
        "Exam_Pressure":[float(exam_pressure)],
        "Family_Support":[float(family_support)],
        "Month":[float(month)]
    })


    prediction = model.predict(input_df)

    if prediction:
        st.success("You are relaxed!")
    else:
        st.error("You are stressed!")
