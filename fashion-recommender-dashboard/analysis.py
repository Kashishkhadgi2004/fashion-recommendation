import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_daq as daq
import plotly.graph_objs as go

# Load the dataset
df = pd.read_csv('data.csv')
df = df.dropna()  # Remove missing values to avoid errors in graphs

# ✅ DASHBOARD LAYOUT (EXACTLY LIKE SANTOSH'S)
dashboard = dcc.Loading([
    dbc.Row([
        dbc.Card([
            html.H4('Data Analysis Dashboard', className="text-center text-white"),
        ], className='bg-success bg-gradient p-2'),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    html.Label('Filter Data: ', className="text-white"),
                ], className='bg-gradient p-2')
            ], width='auto'),

            dbc.Col([
                dcc.Dropdown([x for x in df.columns][2:-1], id='columns',
                             style={'color': 'black'}, placeholder="Select Field..."),
            ]),

            dbc.Col([
                dcc.Dropdown(id='col_value', multi=True, style={'color': 'black'}, placeholder='Select Sub-Field...'),
            ]),
        ], className='m-2', align='center', justify='center'),
    ], className='p-2'),

    dbc.Row([
        # ✅ LEFT COLUMN (METRICS)
        dbc.Col([
            dbc.Card([
                html.Label('Total Records', className='text-white text-center'),
                html.H1(df.shape[0], className='text-white text-center')
            ], color="warning", className='m-2 p-3'),

            dbc.Card([
                html.Label('Total Features', className='text-white text-center'),
                html.H1(df.shape[1], className='text-white text-center')
            ], color="info", className='m-2 p-3'),

            dbc.Card([
                html.Label('Null Values', className='text-white text-center'),
                html.H1(df.isnull().sum().sum(), className='text-white text-center')
            ], color="danger", className='m-2 p-3'),

            dbc.Card([
                html.Label('Null Values Percentage', className='text-white text-center'),
                daq.Gauge(
                    id='acc_gauge',
                    color={"gradient": True,
                           "ranges": {"red": [30, 100], "yellow": [10, 30], "green": [0, 10]}},
                    value=round((df.isnull().mean() * 100).sum(), 2),
                    max=100, min=0, size=110
                ),
            ], color="success", className='m-2 p-3'),
        ], xl=2, lg=2, md=6, sm=12, xs=12),

        # ✅ RIGHT COLUMN (GRAPHS)
        dbc.Col([
            dbc.Row([
                dbc.Col(dcc.Graph(id='gender_bar'), width=6),
                dbc.Col(dcc.Graph(id='category_pie'), width=6),
            ]),

            dbc.Row([
                dbc.Col(dcc.Graph(id='subcat_sunburst'), width=6),
                dbc.Col(dcc.Graph(id='brand_pie'), width=6),
            ]),

            dbc.Row([
                dbc.Col(dcc.Graph(id='color_stackbar'), width=6),
                dbc.Col(dcc.Graph(id='usage_pie'), width=6),
            ]),

            dbc.Row([
                dbc.Col(dcc.Graph(id='season_funnel'), width=12),
            ]),
        ]),
    ])
], color="#119DFF", type="graph", fullscreen=True, className='bg-dark')

# ✅ GRAPH UPDATES

def update_gender(df):
    gender = df['gender'].value_counts().reset_index()
    fig = px.bar(x=gender['index'], y=gender['gender'], color=gender['index'],
                 labels={'x': 'Gender', 'y': 'Product Counts'}, template='plotly_dark')
    return fig

def update_category(df):
    category = df['masterCategory'].value_counts().reset_index()
    fig = px.pie(category, names='index', values='masterCategory', hole=0.4, template='plotly_dark')
    return fig

def update_subcategory(df):
    fig = px.sunburst(df, path=['masterCategory', 'subCategory'], template='plotly_dark')
    return fig

def update_brand(df):
    df['brand'] = df['productDisplayName'].str.split().str[0]
    brand = df['brand'].value_counts().head().reset_index()
    fig = px.pie(brand, names='index', values='brand', hole=0.4, template='plotly_dark')
    return fig

def update_productColor(df):
    colors = df[['gender', 'baseColour']].value_counts().reset_index()
    fig = px.bar(colors, x='gender', y=0, color='baseColour', template='plotly_dark')
    return fig

def update_usage(df):
    usage = df['usage'].value_counts().reset_index()
    fig = px.pie(usage, values='usage', names='index', hole=0.3, template='plotly_dark')
    return fig

def update_season(df):
    season = df['season'].value_counts().reset_index()
    fig = px.funnel(season, x='season', y='index', template='plotly_dark')
    return fig

@callback(
    Output('col_value', 'options'),
    Input('columns', 'value')
)
def update_dropdown(x):
    if x is None:
        return []
    return df[x].unique()

@callback(
    Output('gender_bar', 'figure'),
    Output('category_pie', 'figure'),
    Output('subcat_sunburst', 'figure'),
    Output('brand_pie', 'figure'),
    Output('color_stackbar', 'figure'),
    Output('usage_pie', 'figure'),
    Output('season_funnel', 'figure'),
    Input('columns', 'value'),
    Input('col_value', 'value')
)
def update_data(x, y):
    filtered_df = df if x is None or y is None else df[df[x].isin(y)]
    return (update_gender(filtered_df),
            update_category(filtered_df),
            update_subcategory(filtered_df),
            update_brand(filtered_df),
            update_productColor(filtered_df),
            update_usage(filtered_df),
            update_season(filtered_df))
