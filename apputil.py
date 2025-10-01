import plotly.express as px
import pandas as pd

# Module-level cached dataset
TITANIC_URL = 'https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv'
titanic_df = pd.read_csv(TITANIC_URL)


def survival_demographics():
    """Return (agg_df, fig) where agg_df groups by Pclass, Sex, Age Group and
    contains n_survived, n_total, survival_rate (percentage).

    fig is a Plotly Figure (grouped bar, colored by Sex, faceted by Pclass).
    """
    df = titanic_df.copy()
    bins = [0, 12, 19, 59, 1000]
    labels = ['Child', 'Teen', 'Adult', 'Senior']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, include_lowest=True)

    agg = df.groupby(['Pclass', 'Sex', 'Age Group'])['Survived'].agg(['sum', 'count']).reset_index()
    agg = agg.rename(columns={'sum': 'n_survived', 'count': 'n_total'})
    agg['survival_rate'] = (agg['n_survived'] / agg['n_total']) * 100

    # Sort rows for consistent display
    agg = agg.sort_values(['Sex', 'Pclass', 'Age Group']).reset_index(drop=True)

    fig = px.bar(
        agg,
        x='Age Group',
        y='survival_rate',
        color='Sex',
        facet_col='Pclass',
        barmode='group',
        labels={'survival_rate': 'Survival Rate (%)'},
        title='Titanic Survival Rate by Class, Sex and Age Group'
    )

    return agg, fig


def family_size():
    """Return (family_data, avg_fare, min_fare, max_fare, n_passengers, fig)."""
    df = titanic_df.copy()
    df['Family Size'] = df['SibSp'] + df['Parch'] + 1
    avg_fare = df['Fare'].mean()
    min_fare = df['Fare'].min()
    max_fare = df['Fare'].max()
    n_passengers = df['PassengerId'].count()

    family_data = df[['Family Size', 'Pclass', 'Fare']]
    fig = px.histogram(family_data, x='Family Size', title='Distribution of Family Sizes')

    return family_data, avg_fare, min_fare, max_fare, n_passengers, fig


def last_names():
    """Return a DataFrame with last name counts: columns LastName, Count."""
    df = titanic_df.copy()
    names = df['Name'].dropna().astype(str)
    last_names = names.str.split(',', n=1).str[0].str.strip()
    counts = last_names.value_counts().reset_index()
    counts.columns = ['LastName', 'Count']
    return counts


if __name__ == '__main__':
    # Quick CLI demo when run directly
    agg, fig = survival_demographics()
    print(agg.to_string(index=False))