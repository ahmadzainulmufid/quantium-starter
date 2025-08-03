from dash import Dash, Input, Output, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('formated_output.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce', format='%Y-%m-%d')
df['region'] = df['region'].str.strip().str.lower()
df = df.sort_values(by='date')

regions = {'north', 'south', 'east', 'west'}

app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'fontFamily': 'Arial'}, children=[
    html.H1("Pink Morsel Sales Visualiser", style={
        'textAlign': 'center',
        'color': '#2c3e50',
        'padding': '20px'
    }),

    html.Div([
        html.Label('Select Region:', style={'margin-right': '15px', 'fontWeight': 'bold'}),
        dcc.RadioItems(
            id='region-selector',
            options=[{'label': region.capitalize(), 'value': region} for region in regions],
            value='all',
            inline=True,
            style={'padding': '10px'}
        )
    ], style={'textAlign': 'center'}),

    dcc.Graph(id='sales-line-chart')
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)

def update_chart(selected_region):
    filtered_df = df.copy()
    if selected_region != 'all':
        filtered_df = filtered_df[filtered_df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f"Pink Morsel Sales Over Time ({selected_region.capitalize()})",
        labels={'date': 'Date', 'sales': 'Sales ($)'}
    )

    # Tambah garis vertikal dan anotasi
    fig.add_shape(
        type='line',
        x0='2021-01-15', x1='2021-01-15',
        y0=0, y1=filtered_df['sales'].max(),
        line=dict(color='red', dash='dash'),
    )
    fig.add_annotation(
        x='2021-01-15',
        y=filtered_df['sales'].max(),
        text='Price Increase',
        showarrow=False,
        yanchor='bottom',
        font=dict(color='red')
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)
