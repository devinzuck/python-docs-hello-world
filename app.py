from flask import Flask
app = Flask(__name__)

# Import Statements
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Insert Comment about stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Insert Comment 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# The "layout" is a hierarchical tree of components that describes what the Dash app looks like. 
app.layout = html.Div(children=[
    # Create a Title for the website  
    html.H1(children='Input to Generate Allergen Matrix'),

# Create a dropdown for line selection 
    html.Label('Line Selection'),
    dcc.Dropdown(
        id='Line Selection',
        options= [{'label':option, 'value': option} for option in get_line_types()],  
            # options need to be in the format of:
            [{'label': 'TC', 'value': 'TC'},
            {'label': 'PC', 'value': 'PC'},
            {'label': 'Bare', 'value': 'Bare'}]
        value='TC'
    )

])

# @app.route("/")
# def hello():  
#     return "Hello, Keith"

if __name__ == '__main__':
    app.run_server(debug=True)

