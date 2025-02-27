import streamlit as st

st.title("Test Streamlit App")

age = st.slider("How old are you?", 5, 100, 10)
st.write("I'm ", age, "years old")