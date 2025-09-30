import plotly.express as px
import pandas as pd

# update/add code below ...

titanic_df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

def survival_demographics():
    ''' Defined a function to analyze survival demographics on the Titanic. '''
    bins = [0, 12, 19, 59, 1000]
    labels = ['Child', 'Teen', 'Adult', 'Senior']
    titanic_df['Age Group'] = pd.cut(titanic_df['Age'], bins=bins, labels=labels, include_lowest=True)
    # Compute number of survivors and total passengers per class/age-group
    agg = titanic_df.groupby(['Pclass', 'Age Group'])['Survived'].agg(['sum', 'count']).reset_index()
    agg = agg.rename(columns={'sum': 'n_survived', 'count': 'n_total'})

    # Calculate survival rate as percentage (0-100)
    agg['survival_rate'] = (agg['n_survived'] / agg['n_total']) * 100

    # Create a Plotly bar chart showing survival_rate by Age Group, colored by Pclass
    fig = px.bar(
        agg,
        x='Age Group',
        y='survival_rate',
        color='Pclass',
        barmode='group',
        labels={'survival_rate': 'Survival Rate (%)'},
        title='Titanic Survival Rate by Class and Age Group'
    )

    # Return both the aggregated table and the figure for flexibility
    return agg, fig


if __name__ == '__main__':
    # When run directly, print the table
    table, _ = survival_demographics()
    print(table.to_string(index=False))

