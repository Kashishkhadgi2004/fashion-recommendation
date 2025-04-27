# import dash
# from dash import dcc, Output, Input, State, html
# import dash_bootstrap_components as dbc

# # Import existing project files
# import recommend
# import analysis
# import registration  # Importing the registration page

# # Initialize Dash app
# theme = [dbc.themes.SOLAR]
# app = dash.Dash(__name__, external_stylesheets=theme, suppress_callback_exceptions=True,
#                 meta_tags=[{'name': 'viewport',
#                             'content': 'width=device-width, initial-scale=1.0'}])

# server = app.server
# app.title = 'Fashion Recommender'
# app._favicon = "shop.png"

# # ✅ Store variable to track if registration is completed
# app.layout = dbc.Container([
#     dcc.Store(id="registration-done", data=False),  # Stores registration state
#     dcc.Location(id="url", refresh=False),

#     # ✅ Navbar (Recommend & Analysis buttons are here)
#     dbc.NavbarSimple(
#         children=[
#             dbc.NavItem(dbc.NavLink(
#                 "Recommend", href="/", className="me-1 text-white text-decoration-none fs-5", id='predict_link')),

#             dbc.NavItem(dbc.NavLink(
#                 "Analysis", href="/analysis", className="me-1 text-white text-decoration-none fs-5", id='model_link')),
#         ],
        
#         fixed='top',
#         brand="Fashion Product Recommender",
#         brand_href="/",
#         color="warning",
#         dark=True,
#         className='py-0'
#     ),

#     html.Br(), html.Br(),

#     dbc.Row(id="display")  # ✅ This will dynamically update pages
# ], fluid=True)


# # ✅ Callback to Handle Navigation
# @app.callback(
#     Output("display", "children"),
#     Input("url", "pathname"),
#     State("registration-done", "data")
# )
# def update_page(pathname, registered):
#     if not registered:  # If user is not registered, show registration page
#         return registration.registration_layout
#     elif pathname == "/analysis":  # Show Analysis page
#         return analysis.dashboard
#     return recommend.recommend_div  # Default to Search Page


# # ✅ Callback for Registration Button
# @app.callback(
#     Output("registration-done", "data"),
#     Output("url", "pathname"),
#     Input("register-btn", "n_clicks"),
#     prevent_initial_call=True
# )
# def complete_registration(n_clicks):
#     return True, "/"  # ✅ Redirect to Search Page after registration


# if __name__ == '__main__':
#     app.run_server(host='0.0.0.0', port=8080, debug=False)



# import dash
# from dash import dcc, html, Input, Output, State
# import dash_bootstrap_components as dbc

# # Import existing project files
# import recommend
# import analysis
# import registration
# # import price_comparison  # ✅ Import Price Comparison Page
# from price_comparison import price_comparison_layout

# # Initialize Dash app
# theme = [dbc.themes.SOLAR]
# app = dash.Dash(__name__, external_stylesheets=theme, suppress_callback_exceptions=True,
#                 meta_tags=[{'name': 'viewport',
#                             'content': 'width=device-width, initial-scale=1.0'}])

# server = app.server
# app.title = 'Fashion Recommender'
# app._favicon = "shop.png"

# # ✅ Store variable to track if registration is completed
# app.layout = dbc.Container([
#     dcc.Store(id="registration-done", data=False),  # Stores registration state
#     dcc.Location(id="url", refresh=False),

#     # ✅ Navbar (Now includes Compare Price)
#     dbc.NavbarSimple(
#         children=[
#             dbc.NavItem(dbc.NavLink("Recommend", href="/", className="me-1 text-white text-decoration-none fs-5")),
#             dbc.NavItem(dbc.NavLink("Analysis", href="/analysis", className="me-1 text-white text-decoration-none fs-5")),
#             dbc.NavItem(dbc.NavLink("Compare Price", href="/compare-price", className="me-1 text-white text-decoration-none fs-5")),  # ✅ New Compare Price Option
#         ],
#         fixed='top',
#         brand="Fashion Product Recommender",
#         brand_href="/",
#         color="warning",
#         dark=True,
#         className='py-0'
#     ),

#     html.Br(), html.Br(),

#     dbc.Row(id="display")  # ✅ This dynamically updates pages
# ], fluid=True)


# # ✅ Callback to Handle Navigation
# @app.callback(
#     Output("display", "children"),
#     Input("url", "pathname"),
#     State("registration-done", "data")
# )
# def update_page(pathname, registered):
#     if not registered:  
#         return registration.registration_layout
#     elif pathname == "/analysis":  
#         return analysis.dashboard
#     elif pathname == "/compare-price":  
#         return price_comparison_layout  # ✅ Fix: Correctly Load Price Comparison Page
#     return recommend.recommend_div   # Default to Recommendations Page


# # ✅ Callback for Registration Button
# @app.callback(
#     Output("registration-done", "data"),
#     Output("url", "pathname"),
#     Input("register-btn", "n_clicks"),
#     prevent_initial_call=True
# )
# def complete_registration(n_clicks):
#     return True, "/"   # ✅ Redirect to Search Page after Registration


# if __name__ == '__main__':
#     app.run_server(host='0.0.0.0', port=8080, debug=False)

import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# Import existing project files

from db import user_collection  # Import the MongoDB collection
import recommend
import analysis
import registration
from price_comparison import price_comparison_layout, register_price_comparison_callbacks  

# Initialize Dash app
theme = [dbc.themes.SOLAR]
app = dash.Dash(__name__, external_stylesheets=theme, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

server = app.server
app.title = 'Fashion Recommender'
app._favicon = "shop.png"

# ✅ Store variable to track if registration is completed
app.layout = dbc.Container([
    dcc.Store(id="registration-done", data=False),  # Stores registration state
    dcc.Location(id="url", refresh=False),

    # ✅ Navbar (Now includes Compare Price)
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Recommend", href="/", className="me-1 text-white text-decoration-none fs-5")),
            # dbc.NavItem(dbc.NavLink("Analysis", href="/analysis", className="me-1 text-white text-decoration-none fs-5")),
            dbc.NavItem(dbc.NavLink("Compare Price", href="/compare-price", className="me-1 text-white text-decoration-none fs-5")),  # ✅ Compare Price Option
        ],
        fixed='top',
        brand="Fashion Product Recommender",
        brand_href="/",
        color="warning",
        dark=True,
        className='py-0'
    ),

    html.Br(), html.Br(),

    dbc.Row(id="display")  # ✅ This dynamically updates pages
], fluid=True)


# ✅ Callback to Handle Navigation
@app.callback(
    Output("display", "children"),
    Input("url", "pathname"),
    State("registration-done", "data")
)
def update_page(pathname, registered):
    if not registered:  
        return registration.registration_layout
    elif pathname == "/analysis":  
        return analysis.dashboard
    elif pathname == "/compare-price":  
        return price_comparison_layout  # ✅ Fix: Correctly Load Price Comparison Page
    return recommend.recommend_div   # Default to Recommendations Page


# ✅ Callback for Registration Button
# @app.callback(
#     Output("registration-done", "data"),
#     Output("url", "pathname"),
#     Input("register-btn", "n_clicks"),
#     prevent_initial_call=True
# )
# def complete_registration(n_clicks):
#     return True, "/"   # ✅ Redirect to Search Page after Registration
@app.callback(
    Output("registration-done", "data"),
    Output("url", "pathname"),
    Input("register-btn", "n_clicks"),
    State("username", "value"),
    State("password", "value"),
    State("age", "value"),
    State("gender", "value"),
    State("profession", "value"),
    prevent_initial_call=True
)
def complete_registration(n_clicks, username, password, age, gender, profession):
    if n_clicks:
        user_data = {
            "username": username,
            "password": password,
            "age": age,
            "gender": gender,
            "profession": profession
        }
        user_collection.insert_one(user_data)  # Store into MongoDB
    return True, "/"


# ✅ Register Callbacks for Price Comparison
register_price_comparison_callbacks(app)  # ✅ Ensures search works properly

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=False)

