import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Student Study Tracker")

# Sidebar navigation
st.sidebar.title("Menu")
page = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Study Input", "Feedback", "About"]
)

# ---------------- HOME PAGE ----------------
if page == "Home":

    st.title("📚 Student Study Tracker")

    st.header("Welcome")

    name = st.text_input("Enter your name")

    age = st.number_input("Enter your age", 10, 100)

    course = st.selectbox(
        "Select your course",
        ["IT", "Engineering", "Business", "Arts"]
    )

    study_hours = st.slider("Hours you study per day", 0, 12)

    today = st.date_input("Select today's date")

    st.write("### Your Information")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Course:", course)
    st.write("Study hours:", study_hours)

    st.progress(study_hours / 12)

# ---------------- STUDY INPUT PAGE ----------------
elif page == "Study Input":

    st.title("✏ Study Session")

    subject = st.text_input("Subject studied today")

    difficulty = st.radio(
        "Difficulty level",
        ["Easy", "Medium", "Hard"]
    )

    materials = st.multiselect(
        "Study materials used",
        ["Book", "Laptop", "Notes", "Internet"]
    )

    reminder = st.time_input("Study reminder time")

    file = st.file_uploader("Upload notes (optional)")

    note = st.text_area("Write a short note about today's study")

    if st.button("Save Study Session"):
        st.success("Study session saved!")

# ---------------- FEEDBACK PAGE ----------------
elif page == "Feedback":

    st.title("⭐ Student Feedback")

    rating = st.slider("Rate your productivity today", 1, 10)

    mood = st.selectbox(
        "How do you feel today?",
        ["Happy", "Okay", "Tired", "Stressed"]
    )

    agree = st.checkbox("I completed my study goals")

    color = st.color_picker("Pick your favorite study color")

    with st.expander("Click to leave additional feedback"):
        comment = st.text_area("Additional comments")

    st.write("Your rating:", rating)
    st.write("Mood:", mood)

# ---------------- ABOUT PAGE ----------------
elif page == "About":

    st.title("About This App")

    st.header("What the App Does")
    st.write("""
    This app helps students track their daily study sessions,
    record study hours, and give feedback about their productivity.
    """)

    st.header("Target Users")
    st.write("""
    Students who want to monitor their study habits and
    improve productivity.
    """)

    st.header("Inputs Collected")
    st.write("""
    - Name and age
    - Course
    - Study hours
    - Subject studied
    - Difficulty level
    - Study materials
    - Productivity rating
    """)

    st.header("Outputs Displayed")
    st.write("""
    - Study summary
    - Progress bar for study hours
    - Productivity rating
    - User feedback
    """)

    st.caption("Created using Streamlit UI Components")