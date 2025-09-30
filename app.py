import streamlit as st
import pandas as pd
import plotly.express as px

from apputil import survival_demographics

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write("Was the survival rate on the Titanic for children similar among classes?")
'''
# Titanic Visualization 1

'''
