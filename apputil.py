import plotly.express as px
import pandas as pd

TITANIC_URL = 'https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv'
titanic_df = pd.read_csv(TITANIC_URL)


def survival_demographics():
      ''' Defining a function to analyze survival demographics on the Titanic. '''
    bins = [0, 12, 19, 59, 1000]
    labels = ['Child', 'Teen', 'Adult', 'Senior']
    titanic_df['Age Group'] = pd.cut(titanic_df['Age'], bins=bins, labels=labels, include_lowest=True)
    # Compute number of survivors and total passengers per class/age-group
    grouped_titanic = titanic_df.groupby(['Pclass', 'Age Group', 'Sex']).agg(n_passengers = ('PassengerId', 'count'), n_survivors =('Survived', 'sum'))
    grouped_titanic['survival_rate'] = (grouped_titanic['n_survivors'] / grouped_titanic['n_passengers']) * 100
    
    return grouped_titanic

def family_groups():
    titanic_df['family_size'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1
    sorted_titanic_df = titanic_df.groupby(['Pclass', 'family_size']).agg(n_passengers = ('PassengerId', 'count'), avg_fare =('Fare', 'mean'), min_fare = ('Fare', 'min'), max_fare = ('Fare', 'max'))
    return sorted_titanic_df


def last_names():
    titanic_df['last_name'] = titanic_df['Name'].str.split(',').str[0]
    titanic_df_lastname_count = titanic_df.groupby(['last_name']).agg(last_names = ('last_name', 'count'))
    return titanic_df_lastname_count
