#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dash import Dash, html, dcc
from dash.dependencies import Input, Output

css = 'https://codepen.io/chriddyp/pen/bWLwgP.css'
app = Dash(__name__, external_stylesheets=[css])
server = app.server



app.layout = html.Div([
    # edit Dash App here
    # Dash documentation: https://dash.plotly.com/
    html.H1('My Dashboard'),
])


if __name__ == '__main__':
    app.run_server(debug=True)