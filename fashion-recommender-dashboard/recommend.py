from dash import dash, html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
import base64
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import prediction

# ✅ Load Flipkart & Myntra data
df_flipkart = pd.read_csv('flipkart_data.csv')
df_myntra = pd.read_csv('myntra_data.csv')
df_amazon = pd.read_csv('amazon_data.csv')


# ✅ Combine both datasets
df = pd.concat([df_flipkart, df_myntra,df_amazon], ignore_index=True)

# ✅ Product Card Function (Supports Flipkart & Myntra)
def create_product_card(index):
    row = df.iloc[index]
    img_url = row['img']
    title = row['title']
    url = row['url']

    # ✅ Fetch price & rating differently for Myntra
    if 'flipkart' in url:
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        ratings = soup.find_all('div', {'class': '_3LWZlK _3uSWvT'})
        price_web = soup.find_all('div', {'class': '_30jeq3 _16Jk6d'})
        rating = ratings[0].text if ratings else "N/A"
        price = price_web[0].text if price_web else "N/A"
    else:
        rating = row.get('rating', "N/A")  # Assuming Myntra has 'rating' column
        price = row.get('sold_price', "N/A")

    card = dbc.Card([
        dbc.Carousel(
            items=[{"key": "1", "src": img_url, "img_style": {'max-height': "200px"}}],
            controls=False, indicators=False),
        dbc.CardBody([
            html.Label(f'{title[:30]}...', className="card-title text-black"),
            html.Br(),
            dbc.Badge(f'₹{price}', color="primary", className="me-1"),
            dbc.Badge(f'⭐ {rating}', color="warning", className="me-1"),
            dbc.Button("Buy", outline=True, href=url, size='md', target="_blank", color="danger",
                       className="m-2", style={'height': 'auto', 'width': '150px'}),
        ], className='text-center'),
    ], style={"width": "200px", 'height': '350px'}, className='bg-gradient m-2')

    return card


# ✅ UI Layout
recommend_div = dbc.Container([
    dbc.Row([
        dbc.Badge('Fashion Product Recommender', pill=True, color="success", text_color='black',
                  className="me-1 text-center fs-4 fw-bold", style={'width': "auto"}),
        html.Br(),
        dbc.Row([
            dbc.Card([dbc.Row([
                dbc.Col([html.Img(id='input-img', style={
                    'width': '150px',
                    'height': '150px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                }),
                         html.Label('Uploaded Image')]),

                dbc.Col([dcc.Upload(['Drag and Drop or ', html.Br(), html.A('Select an Image', href='#')],
                                    style={'width': '150px',
                                           'height': '150px',
                                           'lineHeight': '60px',
                                           'borderWidth': '1px',
                                           'borderStyle': 'dashed',
                                           'borderRadius': '5px',
                                           'textAlign': 'center'},
                                    id='upload-image'),
                         html.Label('Upload Here')])]),
                dbc.Row([dbc.Button('Search', outline=True, color="primary", id='show-btn', n_clicks=0,
                                    className='m-2 text-center',
                                    style={'width': '50%', })],
                        justify='center',
                        align='center',
                        style={'textAlign': 'center'})

            ], className='p-2 bg-gradient', style={'text-align': 'center', 'width': '350px'})
        ], className='p-3', style={'text-align': 'center'}, align='center', justify='center'),
        html.Div(dbc.Badge('Recommendations', color='#85e35f', text_color='black')),
        html.Br(),
        dcc.Loading([
            dbc.Row([
                dbc.Col(id='product1'),
                dbc.Col(id='product2'),
                dbc.Col(id='product3'),
                dbc.Col(id='product4'),
                dbc.Col(id='product5'),
                dbc.Col(id='product6'),
                dbc.Col(id='product7'),
                dbc.Col(id='product8'),
                dbc.Col(id='product9'),
                dbc.Col(id='product10'),
            ], className='m-2')
        ], color="#119DFF", type="default", fullscreen=True, className='bg-dark bg-gradient')

    ], justify='center', align='center', style={'text-align': 'center'})
])


# ✅ Update Uploaded Image
@callback(
    Output('input-img', 'src'),
    Input('upload-image', 'contents')
)
def update_input_img(contents):
    if contents is not None:
        decodeit = open('assets/input_img.jpeg', 'wb')
        decodeit.write(base64.b64decode((contents.split('base64,')[1])))
        decodeit.close()
        return contents
    else:
        return 'assets/product.png'


# ✅ Update Recommendation Results
@callback(
    Output('product1', 'children'),
    Output('product2', 'children'),
    Output('product3', 'children'),
    Output('product4', 'children'),
    Output('product5', 'children'),
    Output('product6', 'children'),
    Output('product7', 'children'),
    Output('product8', 'children'),
    Output('product9', 'children'),
    Output('product10', 'children'),
    Input('show-btn', 'n_clicks')
)
def update_result(n_clicks):
    if n_clicks > 0:
        result = prediction.get_result('assets/input_img.jpeg')
        os.remove("assets/input_img.jpeg")

        # ✅ Select 5 from prediction + 5 random from full dataset
        product_indexes = result[:5] + df.sample(5).index.tolist()

        return [create_product_card(idx) for idx in product_indexes]

    else:
        return [html.P('') for _ in range(10)]
