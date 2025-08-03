from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
}

df = pd.read_csv('formated_output.csv')

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

fig = px.line(df, x='date', y='sales', title='Pink Morsel Sales Over Time', labels={'date': 'Date', 'sales': 'Sales ($)'})

fig.add_shape(
    type='line',
    x0='2021-01-15', x1='2021-01-15',
    y0=0, y1=df['sales'].max(),
    line=dict(color='red', dash='dash'),
)

fig.add_annotation(
    x='2021-01-15',
    y=df['sales'].max(),
    text='Price Increase',
    showarrow=False,
    yanchor='bottom',
    font=dict(color='red')
)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
