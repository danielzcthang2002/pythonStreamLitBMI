import streamlit as st

st.title("Welcome to BMI Calculator")

weight = st.number_input("Enter your weight (in kgs)")
height = st.number_input('Enter your height (in cms)')
bmi = 0
try:
    bmi = weight / ((height / 100) ** 2)
except:
    st.text("Enter some value of height")

if st.button('Calculate BMI'):
    st.text("Your BMI Index is {}.".format(bmi))

    if bmi < 16:
        st.error("You are Extremely Underweight")
    elif 16 <= bmi < 18.5:
        st.warning("You are Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Healthy")
    elif 25 <= bmi < 30:
        st.warning("Overweight")
    elif bmi >= 30:
        st.error("Extremely Overweight")
