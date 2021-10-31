import dash
from dash import dcc
import plotly.express as px
from dash import html
import math
from dash.dependencies import Input, Output


app=dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Circle Graph'),
    dcc.Textarea(
        id='graph2',
    ),
    dcc.Graph(
        id='graph1',
        style={
            'width': '80vh', 'height': '80vh'
        }

    ),
    dcc.Slider(
        id='my-slider',
        min=3,
        max=100,
        step=1,
        value=3,
        updatemode='drag'
    )
])

@app.callback(
    Output('graph1','figure'),
    Input('my-slider', 'value'))

def build_graph(n):
    xarr=[math.cos(2*math.pi*i/n) for i in range(n+1)]
    yarr=[math.sin(2*math.pi*i/n) for i in range(n+1)]
    fig=px.line(x=xarr,y=yarr,range_x=[-1,1],range_y=[-1,1])
    
    return fig

@app.callback(
    Output('graph2','value'),
    Input('my-slider', 'value'))
def build_graph2(n):

    area=(1/2*n*math.sin(2*math.pi/n))
    return "Sides: {}, Area: {}".format(str(n),str(area))

if __name__ == '__main__':
    app.run_server(debug=True)