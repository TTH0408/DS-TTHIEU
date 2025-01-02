import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🎈 Hello Bro! This is my new Data Science App")
st.write(
    "Let's start."
)

#1. Create dataframe from file
file_uploaded = st.file_uploader("Please upload your file (CSV File):")
if file_uploaded is not None:
    data = pd.read_csv(file_uploaded)
#2. Preview the file
if file_uploaded is not None:
    if st.checkbox("Preview the dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
#3. Check datatype
if file_uploaded is not None:
    if st.checkbox("Datatype of each columns"):
        st.text("Datatypes")
        st.write(data.dtypes)
#4. Find shape of dataframe
if file_uploaded is not None:
    if st.checkbox("Shape of dataframe"):
        st.write("Number of Rows:", data.shape[0])
        st.write("Number of Columns", data.shape[1])
#5. Find null value
if file_uploaded is not None:
    data_null = data.isnull().values.any()
    if data_null == True:
        if st.checkbox("Null data of the dataset:"):
            st.write(data.isnull().sum())
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulation! No null value founded")
#6.Find duplicate value in dataset
if file_uploaded is not None:
    duplicated = data.duplicated().any()
    if duplicated == True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup = st.selectbox("Do You Want To Remove Duplicates Values",\
                           ("Select One", "Yes", "No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup == "No":
            st.text("Ok fine!!!")
#7. Get statistics:
if file_uploaded is not None:
    if st.checkbox("Get Overall Statistics"):
        st.write(data.describe())
#8. About
if st.button("About App"):
    st.text("Published by Mr Hieu")

