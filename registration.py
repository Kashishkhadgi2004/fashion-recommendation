import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

registration_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div(style={
                "background": "rgba(255, 255, 255, 0.8)",  
                "color": "black",
                "padding": "40px",
                "border-radius": "12px",
                "box-shadow": "0px 4px 15px rgba(0,0,0,0.3)",
                "text-align": "center",
                "margin": "auto",
                "border": "2px solid white",
                "width": "400px",
                "justify-content": "center"
            }, 
               
                children=[
                
                html.H2("Fashion Recommender", className="mb-3"),
                dbc.Label("👤 Username"),
                dbc.Input(id="username", type="text", placeholder="Enter your stylish username",
                          className="mb-2", style={"border-radius": "8px", "background-color": "white", "border": "1px solid #ccc"}),


                dbc.Label("🔒 Password"),
                dbc.Input(id="password", type="password", placeholder="Enter a secure password",
                          className="mb-2", style={"border-radius": "8px" , "background-color": "white", "border": "1px solid #ccc"}),

                dbc.Label("📅 Age"),
                dbc.Input(id="age", type="number", placeholder="Enter your age",
                          className="mb-2", style={"border-radius": "8px","background-color": "white", "border": "1px solid #ccc"}),

                dbc.Label("⚧ Gender"),
                dcc.Dropdown(
                    id="gender",
                    options=[
                        {"label": "👨 Male", "value": "Male"},
                        {"label": "👩 Female", "value": "Female"},
                        {"label": "🌈 Other", "value": "Other"}
                    ],
                    placeholder="Select Gender",
                    className="mb-2",
                    style={"border-radius": "8px","background-color": "white", "border": "1px solid #ccc"}
                ),

                dbc.Label("💼 Profession"),
                dcc.Dropdown(
                    id="profession",
                    options=[
                        {"label": "📚 Student", "value": "Student"},
                        {"label": "🛠 Engineer", "value": "Engineer"},
                        {"label": "⚕️ Doctor", "value": "Doctor"},
                        {"label": "🎨 Designer", "value": "Designer"}
                    ],
                    placeholder="Select Profession",
                    className="mb-3",
                    style={"border-radius": "8px","background-color": "white", "border": "1px solid #ccc"}
                ),

                dbc.Button("🚀 Register & Explore Fashion", id="register-btn", color="dark",
                           className="w-100", n_clicks=0, style={
                               "border-radius": "8px",
                               "font-weight": "bold",
                               "background": "black",
                               "color": "white",
                               "box-shadow": "0px 3px 10px rgba(0,0,0,0.2)",
                               "transition": "0.3s ease-in-out"
                           }),
            ]),
        ], width=6)
    ], className="justify-content-center mt-5"),
], fluid=True, style={
    "background": "url('/assets/fashion_bg.jpg')",  # ✅ Use local image
    "background-size": "cover",  # ✅ Fix syntax
    "background-position": "center",
    "height": "100vh",
    "display": "flex",
    "align-items": "center",
    "justify-content": "center"
})  # ✅ Ensure this closing bracket is present
