import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import csv
import json
import pandas as pd
import plotly.express as px
import urllib.request
import json
import plotly.graph_objects as go

lon = [str(i) for i in range(-180,180)]
lat=[i for i in range(-90,90)]
import pandas as pd
d = pd.read_csv("data/MYDAL2_M_SKY_WV_2019-12-01_rgb_360x180.CSV", names=lon )
d['lat']=lat[::-1]

e = 99999.00
col = ['lat','lon','hum']
l=[]
ll=[]

for i in d.index:
    for j in d.columns:
        if j!='lat':
            l.append([d['lat'][i],int(j),d[j][i]])

for i in l:
    if not e in i:
        ll.append(i)

hum_d = pd.DataFrame(ll, columns = col)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
])


def output_(input_value):
    try:
        return ss
    except:
        return 'enter a valid number'

app = dash.Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)
server = app.server

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
     [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output_div(clicks,value):
    s=output_(value)
    return s



Humidity_layout = html.Div([
    html.H1('Humidity'),
    html.Div(children="Humidity values"),
    dcc.Graph(
        id='country-geo-graph',
        figure= go.Figure(data=go.Scattergeo(
        lon = hum_d['lon'],
        lat = hum_d['lat'],
        marker_color = hum_d['hum'],
        ))
    ),
    html.Div(id='Health-content'),
    html.Br(),
    dcc.Link('Go back to actions_page', href='/')
])

@app.callback(dash.dependencies.Output('Health-content', 'children'),
              [dash.dependencies.Input('Health-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


# Update the actions_page
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return Humidity_layout


if __name__ == '__main__':
    app.run_server(debug=True)
