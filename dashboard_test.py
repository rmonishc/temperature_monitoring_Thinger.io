import dash
from dash import dcc,html
from dash import Input, Output
import datetime
import plotly.express as px
import os
import pandas as pd

dir = './CSV_FILES/'
filename = os.path.join(dir, str(datetime.date.today()) + '.csv')

app = dash.Dash(__name__)

def read_data(filename):
    data=pd.read_csv(filename)
    data.columns = ['Time','Temperature','Humidity']
    return data

app.layout = html.Div(
    html.Div([
        html.H4('Lab temperature and humidity today'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=60*1000, # in milliseconds
            n_intervals=0
        )
    ])
)

@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    data = read_data(filename)
    fig = px.line(x=data['Time'], y=data['Temperature'])
    fig.append_trace()
