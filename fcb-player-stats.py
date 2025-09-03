import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io



df = pd.read_csv('Basic Python\Final Project - Data Analysis Project\FCB Player stats.csv')
# st.write(df)

buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

# st.write(df.describe())
st.write(df.isna().sum().sum())