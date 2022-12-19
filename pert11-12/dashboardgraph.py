from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import numpy as np

fig = px.line(
    x = np.array([0, 6]),
    y = np.array([0, 250]), 
    title="sample dashboard", height=325
)

app = Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)