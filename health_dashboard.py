import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Health Metrics Dashboard", page_icon="🩺")

st.title("🩺 Health Metrics Dashboard")
st.write("Track and interpret your BMI, blood pressure, and heart rate.")

# Layout: Input form in columns
st.header("Enter Your Health Info")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    weight = st.number_input("Weight (kg)", min_value=1.0)
    height = st.number_input("Height (cm)", min_value=30.0)

with col2:
    systolic = st.number_input("Systolic BP (mmHg)", min_value=50)
    diastolic = st.number_input("Diastolic BP (mmHg)", min_value=30)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=30)

# Process inputs
if st.button("Calculate Metrics"):
    st.subheader(f"📋 Results for {name or 'User'}")

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # BMI Status
    if bmi < 18.5:
        bmi_status = "Underweight"
    elif 18.5 <= bmi < 25:
        bmi_status = "Normal"
    elif 25 <= bmi < 30:
        bmi_status = "Overweight"
    else:
        bmi_status = "Obese"

    # Blood Pressure Status
    if systolic < 90 or diastolic < 60:
        bp_status = "Low BP"
    elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
        bp_status = "Normal"
    elif 120 < systolic <= 140 or 80 < diastolic <= 90:
        bp_status = "Elevated"
    else:
        bp_status = "High BP"

    # Heart Rate Status
    if heart_rate < 60:
        hr_status = "Low (Bradycardia)"
    elif 60 <= heart_rate <= 100:
        hr_status = "Normal"
    else:
        hr_status = "High (Tachycardia)"

    # Display Metrics
    col3, col4, col5 = st.columns(3)
    col3.metric("BMI", f"{bmi:.2f}", help="Body Mass Index")
    col4.metric("Blood Pressure", f"{systolic}/{diastolic} mmHg")
    col5.metric("Heart Rate", f"{heart_rate} bpm")

    st.info(f"**BMI Status:** {bmi_status}")
    st.warning(f"**Blood Pressure:** {bp_status}")
    st.info(f"**Heart Rate:** {hr_status}")

    # Visualization
    st.subheader("📊 Health Metrics Overview")

    df = pd.DataFrame({
        'Metric': ['BMI', 'Systolic BP', 'Diastolic BP', 'Heart Rate'],
        'Value': [bmi, systolic, diastolic, heart_rate]
    })

    fig, ax = plt.subplots()
    ax.bar(df['Metric'], df['Value'], color='teal')
    ax.set_ylabel("Values")
    ax.set_title("Your Health Metrics")
    st.pyplot(fig)
    import altair as alt
import pandas as pd

df = pd.DataFrame({
    'Metric': ['BMI', 'Weight', 'Height'],
    'Value': [bmi, weight, height]
})

chart = alt.Chart(df).mark_bar().encode(
    x='Metric',
    y='Value',
    color='Metric'
)

st.altair_chart(chart, use_container_width=True)
st.markdown("---")
st.markdown("Built by Joseph Adom Panford - Biomedical Engineer 💡")
st.markdown("Visit my [LinkedIn](http://linkedin.com/in/joseph-panford-7a51322b1) or connect with me (0598912169)for feedback!")

