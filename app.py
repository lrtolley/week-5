import streamlit as st
import pandas as pd
import plotly.express as px

from apputil import survival_demographics, family_groups, last_names

# Load Titanic dataset
titanic_df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write("Was the survival rate on the Titanic for children similar among classes?")

def visualize_demographic():
    '''Making a bar graph to visualize survival of titanic's child and teen passengers.'''
    survival_demographicsdf = survival_demographics()
    survival_demographicsdf = survival_demographicsdf.reset_index()
    barchartsurvival = px.bar(survival_demographicsdf, x = 'Pclass' , y = 'survival_rate', color = 'Sex',barmode = 'group', facet_col = 'Age Group', title = 'survival rate by age group')
    
    return barchartsurvival  

st.write("Were there any people with a unique last name that were a part of a family group on the Titanic?")

def visualize_families():
    family_groupsdf = family_groups()
    family_groupsdf = family_groupsdf.reset_index()
    last_namesdf = last_names()
    last_namesdf = last_namesdf.reset_index()
    joint_df = pd.merge(titanic_df, last_namesdf, on = 'last_name', how = 'outer')
    barchartoffamilies = px.bar(joint_df, x = 'family_size' , y = 'last_names', barmode = 'overlay', color = 'last_name', text = 'last_name', title = 'lesse') 
    
    return barchartoffamilies
