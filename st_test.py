# import streamlit as st

# # App title
# st.title("Simple Addition App")

# # Input fields
# num1 = st.number_input("Enter first number", value=0)
# num2 = st.number_input("Enter second number", value=0)

# # Button
# if st.button("Add"):
#     result = num1 + num2
#     st.success(f"The result is: {result}")

import streamlit as st
import pandas as pd
import random

# App title
st.title("🎉 Fun Name Checker App")

# Create a DataFrame with names
data = {
    "name": ["Priyanka", "Gauri", "Supriya", "Rasika", "Reshma", "Sheetal","Vaibhav"]
}

df = pd.DataFrame(data)

# Fun messages
fun_messages = [
    "🔥 You are awesome!",
    "😎 You are a superstar!",
    "🚀 Future legend detected!",
    "🎯 You are doing great!",
    "🌟 Keep shining!"
    "🌟 You are Hot!"
]

# Input from user
user_name = st.text_input("Enter your name:")

# Button
if st.button("Check"):
    if user_name.strip() == "":
        st.warning("Please enter a name!")
    else:
        # Check if name exists in DataFrame (case-insensitive)
        if user_name.capitalize() in df["name"].values:
            message = random.choice(fun_messages)
            st.success(f"Hey {user_name}! {message}")
            st.balloons()
        else:
            st.info(f"Hello {user_name}! You are unique 😄")
