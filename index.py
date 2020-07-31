import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

import my_app.temporal_callbacks as tc
import my_app.spatial_callbacks  as spc
import my_app.semantic_callbacks as sec
import my_app.temporal_layout as tl
import my_app.spatial_layout  as spl
import my_app.semantic_layout as sel

import datetime as dt

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.YETI], suppress_callback_exceptions=True)
app.title='UVict'

categories = dbc.Select(
    id="class-picker",
    options=[
        {"label": "All", "value": -1},
        {"label": "Conflicto armado", "value": 1},
        {"label": "Tráfico", "value": 2},
        {"label": "Categoría 3", "value": 3},
        {"label": "Eventos de tránsito", "value": 4},
    ],
    value=-1,
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Analisis Temporal", href="/temporal")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Analisis espacial", href="/spatial", header=True),
                dbc.DropdownMenuItem("Análisis semántico", href="/semantic", header=True),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="UVict", brand_href="#", color="primary", dark=True,
)

side_panel_layout = html.Div(
    id='panel-side',
    className='col-2',
    children=[
        html.Div(
            id='panel-side-text',
            children=[
                html.H3(id='panel-side-title', children='Clasificador de noticias'),
                html.P(children=['Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
                                  sed do eiusmod tempor incididunt ut labore et dolore magna \
                                  aliqua. Ut enim ad minim veniam, quis nostrud exercitation \
                                  ullamco laboris nisi ut aliquip ex ea commodo consequat. '])
            ]
        )
    ]
)



main_panel_layout = html.Div(
    id='panel-main',
    className='col-10',
    children=[
        html.Div( id='panel-content', className='row')
    ]
)

root_layout = dbc.Container(fluid=True, children=[
        # represents the URL bar, doesn't render anything
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='page_data'),

        navbar,
        html.Div(
            id="row",
            className='row',
            children=[
                side_panel_layout,
                main_panel_layout,
            ]
        )
    ]
)

app.layout = root_layout



# Activa la ventanita
@app.callback(Output('panel-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/temporal':
        return [
            html.Div(
                id='panel-content',
                className='row',
                children=[tl.content]
            )
        ]
         
    elif pathname == "/spatial":
        return [
            html.Div(
                id='panel-content',
                className='row',
                children=[spl.content]
            )
        ]
    elif pathname == "/semantic":
        return [
            html.Div(
                id='panel-content',
                className='row',
                children=[sel.content]
            )
        ]

    return [
            "[Insert here the home page with the project description]"
        ]



tc.register_callbacks(app)
spc.register_callbacks(app)
sec.register_callbacks(app)



if __name__ == '__main__':
    app.run_server(debug=True)
    #app.run_server(host="0.0.0.0", port=8080)
