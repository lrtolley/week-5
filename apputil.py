import plotly.express as px
import pandas as pd
#import plotly.io as pio
#pio.renderers.default = 'iframe'

# update/add code below ...

titanic_df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

def survival_demographics():
    ''' Defined a function to analyze survival demographics on the Titanic. '''
    bins = [0, 12, 19, 59, 1000]
    labels = ['Child', 'Teen', 'Adult', 'Senior']
    titanic_df['Age Group'] = pd.cut(titanic_df['Age'], bins=bins, labels=labels, include_lowest=True)

fig = px.histogram(titanic_df, 
                   x='Age', 
                   color='Survived',
                   template='plotly_white',
                   color_discrete_sequence=px.colors.qualitative.D3
                  )
fig.update_layout(title='Titanic Age Distribution by Survival Status',)
fig.show()

