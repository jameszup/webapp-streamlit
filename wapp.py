import streamlit as st

st.title("My First Streamlit Web App")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}! 👋")

number = st.slider("Pick a number", 1, 100)

st.write("You selected:", number)
st.write("naeedit ba sya guys?")
