import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

import my_app.temporal_callbacks as tc
import my_app.spatial_callbacks  as spc
import my_app.semantic_callbacks as sec
import my_app.home_callbacks  as hmc
import my_app.temporal_layout as tl
import my_app.spatial_layout  as spl
import my_app.semantic_layout as sel
import my_app.home_layout  as hml

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
        dbc.Row(
            [
                dbc.Col(children=[
                    html.Div(id='none1',children=[],style={'display': 'none'}),
                    ], id="logo1"),
                dbc.Col(dbc.NavbarBrand("UVict", className="ml-2")),
            ]),
        dbc.NavItem(dbc.NavLink("Modelo Clasificación", href="/semantic")),
        dbc.NavItem(dbc.NavLink("Revisión de noticias", href="/temporal")),
        dbc.NavItem(dbc.NavLink("Visualización", href="/spatial")),
    ],
    # brand="UVict", brand_href="#",
    color="primary", dark=True,
)

side_panel_layout = html.Div(
    id='panel-side',
    className='col-2',
    children=[
        html.Div(
            id='panel-side-text',
            children=[
                html.H3(id='panel-side-title', children='Clasificador de noticias'),
                html.P(children=['Sistema de recomendación de noticias para la Bitácora de Eventos Diarios de la Unidad de Víctimas'])
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
        dcc.Location(id='url', refresh=False, pathname=''),
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

# Presenta la imagen del logo
@app.callback(Output("logo1", 'children'), [Input('none1', 'children')])
def image_logo(none):
    return html.Img(
      src=app.get_asset_url('logo 2.png'),
      style={
          "height":"150px",
          "width": "auto",
          "margin-bottom": "25px"
      }
    )

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
            html.Div(
                id='panel-content',
                className='row',
                children=[hml.content]
            )
        ]

tc.register_callbacks(app)
spc.register_callbacks(app)
sec.register_callbacks(app)
hmc.register_callbacks(app)



if __name__ == '__main__':
    app.run_server(debug=True)
    #app.run_server(host="0.0.0.0", port=8080)
