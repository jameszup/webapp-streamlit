import streamlit as st

# Fake user database
users = {
    "admin": "1234",
    "james": "password"
}

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login():
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")


def dashboard():
    st.title("🏠 Dashboard")

    st.write("Welcome to your web app!")

    st.subheader("Example Controls")

    name = st.text_input("Enter your name")

    number = st.slider("Pick a number", 1, 100)

    if st.button("Submit"):
        st.success(f"Hello {name}, your number is {number}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()


# Main App
if st.session_state.logged_in:
    dashboard()
else:
    login()