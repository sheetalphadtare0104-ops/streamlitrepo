import streamlit as st
import pandas as pd 
import numpy as np 
st.title("Hello Everyone This is Our First Application!!!")
st.write("Our application in in Python ")
data=pd.DataFrame({
    "Name":["Sachin","Rohit","Virat","Rahul","Yuvi"],
    "Marks":[90,45,25,78,56]
})
st.write("Below are the Details of Participants..")
st.write(data)
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=["A","B","C"]
    )
#st.bar_chart(chart_data)
st.scatter_chart(chart_data)