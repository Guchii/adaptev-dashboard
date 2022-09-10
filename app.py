from dash import Dash, html, dcc
import dash
from dash import Dash, html, dcc
from pyparsing import White
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True)

app.layout = html.Div([
    dcc.Loading([
        # ...
    ]),
    dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=True)