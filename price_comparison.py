
# # # from dash import dcc, html, Input, Output, State, callback
# # # import dash_bootstrap_components as dbc
# # # import requests

# # # # Conversion rate (Update if needed)
# # # USD_TO_INR = 83  

# # # # Layout for price comparison page
# # # price_comparison_layout = dbc.Container([
# # #     html.H2("Compare Prices Across Platforms 🛒", className="text-center text-white mb-4"),
    
# # #     # Search bar
# # #     dbc.Row([
# # #         dbc.Col(dcc.Input(id="search-product", type="text", placeholder="Search for a product...", className="form-control"), width=8),
# # #         dbc.Col(dbc.Button("Search", id="search-btn", color="warning", className="w-100"), width=2)
# # #     ], className="justify-content-center mb-3"),

# # #     html.Div(id="price-results")  # Display results here
# # # ], fluid=True, className="bg-dark text-white p-5")


# # # # Function to fetch product prices from SerpAPI
# # # def fetch_prices(product_name):
# # #     API_KEY = "2b92b41a53d7fbb8b3e7a0c39d60933e3605abd0e5a307199f230b301d3d7870"  # Replace with your actual SerpAPI key
# # #     search_url = f"https://serpapi.com/search.json?q={product_name}&api_key={API_KEY}"

# # #     response = requests.get(search_url)
# # #     data = response.json()

# # #     product_list = []
    
# # #     for item in data.get("shopping_results", []):
# # #         price = item.get("price", "N/A")

# # #         # Convert USD to INR if price is in dollars
# # #         if "$" in price:
# # #             try:
# # #                 price = float(price.replace("$", "").replace(",", "")) * USD_TO_INR
# # #                 price = f"₹{round(price, 2)}"
# # #             except ValueError:
# # #                 price = "Price not available"

# # #         # Ensure the platform name is captured
# # #         platform = item.get("source", "Unknown")
        
# # #         product_list.append({
# # #             "title": item.get("title", "No Title"),
# # #             "price": price,
# # #             "image": item.get("thumbnail", ""),
# # #             "link": item.get("link", "#"),
# # #             "source": platform  # Platform name
# # #         })

# # #     # Filter to ensure Amazon, Flipkart, and Myntra are included
# # #     prioritized_products = [p for p in product_list if p["source"] in ["Amazon", "Flipkart", "Myntra"]]
    
# # #     # Add other products only if space is available
# # #     other_products = [p for p in product_list if p["source"] not in ["Amazon", "Flipkart", "Myntra"]]
    
# # #     # Merge the lists with priority given to Flipkart, Amazon, and Myntra
# # #     final_products = prioritized_products + other_products[:5]  # Keep results limited

# # #     return final_products


# # # # Callback for search functionality
# # # @callback(
# # #     Output("price-results", "children"),
# # #     Input("search-btn", "n_clicks"),
# # #     State("search-product", "value"),
# # #     prevent_initial_call=True
# # # )
# # # def update_price_results(n_clicks, product_name):
# # #     """Update the UI with price comparison results"""
# # #     products = fetch_prices(product_name)

# # #     if not products:
# # #         return html.P("No results found for Flipkart, Amazon, or Myntra. Try a different product.", className="text-center text-danger")

# # #     return dbc.Row([
# # #         dbc.Col(
# # #             dbc.Card([
# # #                 dbc.CardBody([
# # #                     html.Img(src=item["image"], style={"width": "100%", "height": "200px", "object-fit": "contain"}),
# # #                     html.H5(item["title"], className="card-title"),
# # #                     html.P(f"💰 Price: {item['price']}", className="card-text fw-bold"),
# # #                     html.P(f"🛒 Platform: {item['source']}", className="card-text text-success fw-bold"),
# # #                     dbc.Button("View Product", href=item["link"], color="warning", target="_blank", className="mt-2")
# # #                 ])
# # #             ], className="m-2"),
# # #             width=4
# # #         ) for item in products
# # #     ])



# # from dash import dcc, html, Input, Output, State, callback
# # import dash_bootstrap_components as dbc
# # import requests

# # # Conversion rate (Update if needed)
# # USD_TO_INR = 83  

# # # Layout for price comparison page
# # price_comparison_layout = dbc.Container([
# #     html.H2("Compare Prices Across Platforms 🛒", className="text-center text-white mb-4"),
    
# #     # Search bar
# #     dbc.Row([
# #         dbc.Col(dcc.Input(id="search-product", type="text", placeholder="Search for a product...", className="form-control"), width=8),
# #         dbc.Col(dbc.Button("Search", id="search-btn", color="warning", className="w-100"), width=2)
# #     ], className="justify-content-center mb-3"),

# #     html.Div(id="price-results")  # Display results here
# # ], fluid=True, className="bg-dark text-white p-5")


# # # Function to fetch product prices from SerpAPI
# # def fetch_prices(product_name):
# #     API_KEY = "2b92b41a53d7fbb8b3e7a0c39d60933e3605abd0e5a307199f230b301d3d7870"  # Replace with your actual SerpAPI key
# #     search_url = f"https://serpapi.com/search.json?q={product_name}&api_key={API_KEY}"

# #     response = requests.get(search_url)
# #     data = response.json()

# #     product_list = []
    
# #     for item in data.get("shopping_results", []):
# #         price = item.get("price", "N/A")

# #         # Convert USD to INR if price is in dollars
# #         if "$" in price:
# #             try:
# #                 price = float(price.replace("$", "").replace(",", "")) * USD_TO_INR
# #                 price = f"₹{round(price, 2)}"
# #             except ValueError:
# #                 price = "Price not available"

# #         # Capture platform name correctly
# #         platform = item.get("source", "Unknown").lower()  # Convert to lowercase for matching
        
# #         product_list.append({
# #             "title": item.get("title", "No Title"),
# #             "price": price,
# #             "image": item.get("thumbnail", ""),
# #             "link": item.get("link", "#"),
# #             "source": platform  # Platform name
# #         })

# #     # Ensure Amazon, Flipkart, and Myntra results are included
# #     required_sources = ["amazon", "flipkart", "myntra"]
# #     prioritized_products = []

# #     # Check for each platform and add at least one product if available
# #     for source in required_sources:
# #         product = next((p for p in product_list if source in p["source"]), None)
# #         if product:
# #             prioritized_products.append(product)

# #     # Add other products only if space is available
# #     other_products = [p for p in product_list if p["source"] not in required_sources]

# #     # Merge lists with priority given to Amazon, Flipkart, and Myntra
# #     final_products = prioritized_products + other_products[:5]  # Keep results limited

# #     return final_products


# # # Callback for search functionality
# # @callback(
# #     Output("price-results", "children"),
# #     Input("search-btn", "n_clicks"),
# #     State("search-product", "value"),
# #     prevent_initial_call=True
# # )
# # def update_price_results(n_clicks, product_name):
# #     """Update the UI with price comparison results"""
# #     products = fetch_prices(product_name)

# #     if not products:
# #         return html.P("No results found for Flipkart, Amazon, or Myntra. Try a different product.", className="text-center text-danger")

# #     return dbc.Row([
# #         dbc.Col(
# #             dbc.Card([
# #                 dbc.CardBody([
# #                     html.Img(src=item["image"], style={"width": "100%", "height": "200px", "object-fit": "contain"}),
# #                     html.H5(item["title"], className="card-title"),
# #                     html.P(f"💰 Price: {item['price']}", className="card-text fw-bold"),
# #                     html.P(f"🛒 Platform: {item['source'].capitalize()}", className="card-text text-success fw-bold"),
# #                     dbc.Button("View Product", href=item["link"], color="warning", target="_blank", className="mt-2")
# #                 ])
# #             ], className="m-2"),
# #             width=4
# #         ) for item in products
# #     ])

# from dash import dcc, html, Input, Output, State, callback
# import dash_bootstrap_components as dbc
# import requests

# # Conversion rate (Update if needed)
# USD_TO_INR = 83  

# # Layout for price comparison page
# price_comparison_layout = dbc.Container([
#     html.H2("Compare Prices Across Platforms 🛒", className="text-center text-white mb-4"),
    
#     # Search bar
#     dbc.Row([
#         dbc.Col(dcc.Input(id="search-product", type="text", placeholder="Search for a product...", className="form-control"), width=8),
#         dbc.Col(dbc.Button("Search", id="search-btn", color="warning", className="w-100"), width=2)
#     ], className="justify-content-center mb-3"),

#     html.Div(id="price-results")  # Display results here
# ], fluid=True, className="bg-dark text-white p-5")


# # Function to fetch product prices from SerpAPI
# def fetch_prices(product_name):
#     API_KEY = "2b92b41a53d7fbb8b3e7a0c39d60933e3605abd0e5a307199f230b301d3d7870"  # Replace with your actual SerpAPI key
#     search_url = f"https://serpapi.com/search.json?q={product_name}&api_key={API_KEY}"

#     response = requests.get(search_url)
#     if response.status_code != 200:
#         print("Error fetching data from SerpAPI:", response.text)
#         return []

#     data = response.json()

#     product_list = []
    
#     for item in data.get("shopping_results", []):
#         price = item.get("price", "N/A")

#         # Convert USD to INR if price is in dollars
#         if "$" in price:
#             try:
#                 price = float(price.replace("$", "").replace(",", "")) * USD_TO_INR
#                 price = f"₹{round(price, 2)}"
#             except ValueError:
#                 price = "Price not available"

#         # Extract platform name
#         platform = item.get("source", "Unknown").lower()  # Convert to lowercase for better matching

#         # Debugging log
#         print(f"Found product: {item.get('title', 'No Title')} from {platform}")

#         product_list.append({
#             "title": item.get("title", "No Title"),
#             "price": price,
#             "image": item.get("thumbnail", ""),
#             "link": item.get("link", "#"),
#             "source": platform  # Store platform name
#         })

#     # Ensure at least one result from Amazon, Flipkart, and Myntra
#     required_sources = ["amazon", "flipkart", "myntra"]
#     prioritized_products = []

#     for source in required_sources:
#         product = next((p for p in product_list if source in p["source"]), None)
#         if product:
#             prioritized_products.append(product)

#     # Add other products if space is available
#     other_products = [p for p in product_list if p["source"] not in required_sources]

#     # Debugging output
#     print("Prioritized products:", prioritized_products)

#     # Merge lists with priority given to Amazon, Flipkart, and Myntra
#     final_products = prioritized_products + other_products[:5]  # Keep results limited

#     return final_products


# # Callback for search functionality
# @callback(
#     Output("price-results", "children"),
#     Input("search-btn", "n_clicks"),
#     State("search-product", "value"),
#     prevent_initial_call=True
# )
# def update_price_results(n_clicks, product_name):
#     """Update the UI with price comparison results"""
#     products = fetch_prices(product_name)

#     if not products:
#         return html.P("No results found for Flipkart, Amazon, or Myntra. Try a different product.", className="text-center text-danger")

#     return dbc.Row([
#         dbc.Col(
#             dbc.Card([
#                 dbc.CardBody([
#                     html.Img(src=item["image"], style={"width": "100%", "height": "200px", "object-fit": "contain"}),
#                     html.H5(item["title"], className="card-title"),
#                     html.P(f"💰 Price: {item['price']}", className="card-text fw-bold"),
#                     html.P(f"🛒 Platform: {item['source'].capitalize()}", className="card-text text-success fw-bold"),
#                     dbc.Button("View Product", href=item["link"], color="warning", target="_blank", className="mt-2")
#                 ])
#             ], className="m-2"),
#             width=4
#         ) for item in products
#     ])

import pandas as pd
import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# ✅ Load Flipkart, Amazon, and Myntra data
try:
    flipkart_df = pd.read_csv("flipkart_data.csv")
    amazon_df = pd.read_csv("amazon_data.csv")
    myntra_df = pd.read_csv("myntra_data.csv")
    print("✅ CSV files loaded successfully!")
except Exception as e:
    print(f"❌ Error loading CSV files: {e}")
    flipkart_df, amazon_df, myntra_df = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

# ✅ Merge all datasets
df = pd.concat([flipkart_df, amazon_df, myntra_df], ignore_index=True)

# ✅ Price Comparison Layout
price_comparison_layout = dbc.Container([
    html.H2("Compare Prices", className="text-center mt-3"),

    # ✅ Search Bar
    dbc.Row([
        dbc.Col(dcc.Input(id="search-input", type="text", placeholder="Enter product name...", className="form-control"), width=8),
        dbc.Col(dbc.Button("Search", id="search-btn", color="dark", n_clicks=0), width=2)
    ], className="mt-3 mb-3 justify-content-center"),

    # ✅ Results Container
    dbc.Row([
        dbc.Col(html.Div(id="price-results"), width=12)
    ])
], fluid=True)

# ✅ Callback for Searching Products
def register_price_comparison_callbacks(app):
    @app.callback(
        Output("price-results", "children"),
        Input("search-btn", "n_clicks"),
        State("search-input", "value"),
        prevent_initial_call=True
    )
    def compare_prices(n_clicks, product_name):
        print(f"🔍 Searching for: {product_name}")

        if not product_name:
            return html.Div("❌ Please enter a product name!", className="text-danger")

        # ✅ Case-Insensitive Search in `title` Column
        filtered_df = df[df['title'].str.contains(product_name, case=False, na=False)]

        if filtered_df.empty:
            print("❌ No matching products found.")
            return html.Div("❌ No matching products found.", className="text-danger")

        print(f"✅ Found {len(filtered_df)} products!")

        # ✅ Display Results
        product_cards = []
        for _, row in filtered_df.iterrows():
            product_card = dbc.Card([
                dbc.CardImg(src=row["img"], top=True, style={"height": "200px"}),
                dbc.CardBody([
                    html.H5(row["title"][:30] + "...", className="card-title"),
                    dbc.Badge(f'₹{row["sold_price"]}', color="primary", className="me-1"),
                    dbc.Button("Buy Now", href=row["url"], color="danger", target="_blank")
                ])
            ], style={"width": "200px", "margin": "10px"})

            product_cards.append(dbc.Col(product_card, width=3))

        return dbc.Row(product_cards, className="justify-content-center")
