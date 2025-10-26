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

def visualize_families():
    """
    Return a DataFrame and Plotly bar chart showing whether any passengers
    with a unique last name were part of a family group (Family Size > 1).
    """
    df = titanic_df.copy()

    # Step 1: Extract last names
    df['LastName'] = df['Name'].dropna().astype(str).str.split(',', n=1).str[0].str.strip()

    # Step 2: Count last name occurrences
    last_name_counts = df['LastName'].value_counts()

    # Step 3: Mark unique last names
    df['UniqueLastName'] = df['LastName'].map(last_name_counts) == 1

    # Step 4: Compute family size
    df['Family Size'] = df['SibSp'] + df['Parch'] + 1
    df['InFamilyGroup'] = df['Family Size'] > 1

    # Step 5: Cross-tabulate
    summary = df.groupby(['UniqueLastName', 'InFamilyGroup']).size().reset_index(name='Count')

    # Step 6: Plot
    fig = px.bar(
        summary,
        x='UniqueLastName',
        y='Count',
        color='InFamilyGroup',
        barmode='group',
        labels={
            'UniqueLastName': 'Has Unique Last Name',
            'InFamilyGroup': 'In Family Group',
            'Count': 'Number of Passengers'
        },
        title='Passengers with Unique Last Names in Family Groups'
    )

    return summary, fig

