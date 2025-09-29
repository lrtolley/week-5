import plotly.express as px
import pandas as pd
#import plotly.io as pio
#pio.renderers.default = 'iframe'

# update/add code below ...

titanic_df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

print(titanic_df.head())