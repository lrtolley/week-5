import streamlit as st
import pandas as pd
import plotly.express as px

from apputil import survival_demographics, last_names

# Load Titanic dataset
titanic_df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write("Was the survival rate on the Titanic for children similar among classes?")
def visualize_demographic():
    '''
    # Titanic Visualization - How child and teen survival rates varied by class
    '''
    agg, fig = survival_demographics()
    st.plotly_chart(fig)
visualize_demographic()

st.write("Were there any people with a unique last name that were a part of a family group on the Titanic?")
last_names_count_df = last_names()
print(last_names_count_df.sort_values(by='Count', ascending=False).head())