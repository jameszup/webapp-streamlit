import streamlit as st
import random
import pandas as pd
from datetime import date

st.set_page_config(page_title="Gym's Belen", layout="wide")


# Session storage

if "members" not in st.session_state:
    st.session_state.members = []

# Unique Membership Number

def generate_member_id():
    return f"GYM-{random.randint(100000,999999)}"

# Sidebar 

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Register Member", "Member Dashboard", "Membership Card", "About"]
)

st.sidebar.divider()

st.sidebar.write("Quick Options")
show_data = st.sidebar.checkbox("Show Stored Data")
notifications = st.sidebar.toggle("Enable Notifications")

# Register Member Page

if page == "Register Member":
    st.image("https://api.deepai.org/job-view-file/d10fcd44-abf9-4fad-a548-238ebb81f448/outputs/output.jpg",
                width=240 )
    st.title("Gym's Belen")
    st.text("sarcasm lang yung name!")

    st.subheader("Enter Member Information")

    with st.form("membership_form", clear_on_submit=True):

        name = st.text_input(
            "Full Name",
            autocomplete="off"
        )

        age = st.number_input(
            "Age",
            min_value=10,
            max_value=100,
            step=1
        )

        membership = st.selectbox(
            "Membership Type",
            ["Normal", "Gold", "Diamond"]
        )

        start_date = st.date_input(
            "Membership Start Date",
            value=date.today()
        )

        duration = st.slider(
            "Membership Duration (months)",
            1, 24, 6
        )

        email = st.text_input(
            "Email Address",
            autocomplete="off"
        )

        phone = st.text_input(
            "Phone Number",
            autocomplete="off"
        )

        notes = st.text_area("Notes")

        agree = st.checkbox("I confirm that the information is correct")

        submitted = st.form_submit_button("Create Membership")

    if submitted and agree:

        # Prevent duplicate member
        duplicate = any(
            m["Name"] == name and
            m["Age"] == age and
            m["Membership"] == membership
            for m in st.session_state.members
        )

        if duplicate:
            st.error("This member is already registered.")
        else:

            member_id = generate_member_id()

            new_member = {
                "ID": member_id,
                "Name": name,
                "Age": age,
                "Membership": membership,
                "Start": start_date,
                "Duration": duration
            }

            st.session_state.members.append(new_member)

            st.success("Membership Created Successfully!")
            st.info(f"Membership Number: {member_id}")
            st.balloons()

          
            st.rerun()

# Dashboard Page

elif page == "Member Dashboard":

    st.title("Member Dashboard")

    total_members = len(st.session_state.members)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Members", total_members)

    with col2:
        gold_count = sum(1 for m in st.session_state.members if m["Membership"] == "Gold")
        st.metric("Gold Members", gold_count)

    with col3:
        diamond_count = sum(1 for m in st.session_state.members if m["Membership"] == "Diamond")
        st.metric("Diamond Members", diamond_count)

    st.divider()

    if total_members > 0:

        df = pd.DataFrame(st.session_state.members)

        st.dataframe(df)


        

    else:
        st.warning("No members registered yet.")

# Membership Card view

elif page == "Membership Card":

    st.title("Membership Card Preview")

    if len(st.session_state.members) == 0:
        st.warning("No members available.")
    else:

        member_names = [m["Name"] for m in st.session_state.members]

        selected = st.selectbox(
            "Select Member",
            member_names
        )

        member = next(m for m in st.session_state.members if m["Name"] == selected)

        st.subheader("Gym Membership Card")

        st.markdown("---")

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(
                "https://api.deepai.org/job-view-file/d10fcd44-abf9-4fad-a548-238ebb81f448/outputs/output.jpg",
                width=290
            )

        with col2:
            st.write(f"**Name:** {member['Name']}")
            st.write(f"**Age:** {member['Age']}")
            st.write(f"**Membership Type:** {member['Membership']}")
            st.write(f"**Member ID:** {member['ID']}")

        st.progress(0.9)

        st.caption("Valid only for registered gym members.")

# About Page (Required)

elif page == "About":

    st.title("ℹ About This App")

    st.markdown("""
    ### Gym Membership Management System

    This application is made for managing gym memberships.

    Features included:

    - Member registration
    - Unique membership ID 
    - Dashboard analytics
    - Membership card viewing
    

    ### Membership Types

    *Normal**
    - Basic gym access

    **Gold**
    - Gym + group classes

    **Diamond**
    - Full access + personal trainer

    ### Technology

    To make every gym member a unique number.

    """)

    st.info("Contact us for more information.")

    st.feedback("thumbs")

# Optional Debug Data View

if show_data:
    st.sidebar.write("Stored Data")
    st.sidebar.write(st.session_state.members)