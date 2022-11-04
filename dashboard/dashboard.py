import datetime

import dash
from dash import dcc, html
import plotly
from dash.dependencies import Input, Output
from random import *
import psutil
# pip install pyorbital
from pyorbital.orbital import Orbital
#satellite = Orbital('TERRA')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H4('Innovation Live Feed'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*5000, # in milliseconds
            n_intervals=0
        )
    ])
)


@app.callback(Output('live-update-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    lon, lat, alt = [randint(1, 20), randint(1, 50), randint(1, 15)]
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('networks: {0:.2f}'.format(lon), style=style),
        html.Span('channels: {0:.2f}'.format(lat), style=style),
        html.Span('interfaces: {0:0.2f}'.format(alt), style=style)
    ]


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    #satellite = Orbital('TERRA')
    data = {
        'time': [],
        'Latitude': [],
        'Longitude': [],
        'Altitude': [],
        'ioRead' : [],
        'ioWrite' : [],
        'hostCPU' : [],
        'hostMEM' : []
    }

    # Collect some data
    for i in range(180):
        time = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        data['ioRead'].append(psutil.disk_io_counters().read_count / 100000)
        data['ioWrite'].append(psutil.disk_io_counters().write_count / 100000)
        data['hostCPU'].append(psutil.cpu_percent())
        data['hostMEM'].append(psutil.virtual_memory().percent)
        data['time'].append(time)

    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=4, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig.append_trace({
        'x': data['time'],
        'y': data['hostCPU'],
        'text': data['time'],
        'name': 'Central Process Unit',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 2, 1)
    fig.append_trace({
        'x': data['time'],
        'y': data['hostMEM'],
        'text': data['time'],
        'name': 'Random Access Memory',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 2, 1)
    fig.append_trace({
        'x': data['time'],
        'y': data['ioRead'],
        'text': data['time'],
        'name': 'In and Out Read metrics',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 3, 1)
    fig.append_trace({
        'x': data['time'],
        'y': data['ioWrite'],
        'text': data['time'],
        'name': 'In and Out Write metrics',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 3, 1)

    return fig
    
    
if __name__ == '__main__':
    app.run_server(debug=True,host="0.0.0.0")