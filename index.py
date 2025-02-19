# -*- coding: utf-8 -*-
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

import my_app.temporal_callbacks as tc
import my_app.spatial_callbacks  as spc
# import my_app.semantic_callbacks as sec
import my_app.home_callbacks  as hmc
import my_app.context_callbacks  as ctc
import my_app.temporal_layout as tl
import my_app.spatial_layout  as spl
# import my_app.semantic_layout as sel
import my_app.home_layout  as hml
import my_app.context_layout as ctl

import datetime as dt

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.YETI], suppress_callback_exceptions=True)
app.title='UVict'

navbar = dbc.NavbarSimple(children=[
    dbc.Col(dbc.NavbarBrand("UVict", className="ml-2")),
    # dbc.NavItem(dbc.NavLink("Modelo de clasificación", href="/semantic")),
    dbc.NavItem(dbc.NavLink("Modelo de clasificación", href="/context")),
    dbc.NavItem(dbc.NavLink("Revisión de noticias", href="/temporal")),
    dbc.NavItem(dbc.NavLink("Visualización", href="/spatial"))
    ],
    color="primary", dark=True
)

side_panel_layout = html.Div(
    id='panel-side',
    className='col-2',
    children=[
        html.Div(
            id='panel-side-text',
            children=[
                dbc.Col(children=[
                    html.Div(id='none1',children=[],style={'display': 'none'}),
                    ], id="logo1"),
                # html.H3(id='panel-side-title', children='Clasificador de noticias'),
                dcc.Markdown("""
                    **Sistema de recomendación de noticias para la Bitácora Diaria de Eventos de la Unidad de Víctimas**
                    """),
                html.Br(),
                html.P("Desarrollado por:"),
                html.P("Team-13"),
                html.P("DS4A Colombia 2020"),
            ]
        )
    ]
)

main_panel_layout = html.Div(
    id='panel-main',
    className='col-10',
    children=[
        html.Div( id='panel-content', className='row' )
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

# Presenta la imagen del logo
@app.callback(Output("logo1", 'children'), [Input('none1', 'children')])
def image_logo(none):
    return html.Img(
      src=app.get_asset_url('logo 2.png'),
      style={
          "height":"100px",
          "width": "auto",
          "margin-bottom": "1px"
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
    # elif pathname == "/semantic":
    #     return [
    #         html.Div(
    #             id='panel-content',
    #             className='row',
    #             children=[sel.content]
    #         )
    #     ]
    elif pathname == "/context":
        return [
            html.Div(
                id='panel-content',
                className='row',
                children=[ctl.content]
            )
        ]
    else:
        return [
                # "AQUI HOME"
                html.Div(
                    id='panel-content',
                    className='row',
                    children=[hml.content]
                )
            ]

tc.register_callbacks(app)
spc.register_callbacks(app)
# sec.register_callbacks(app)
hmc.register_callbacks(app)
ctc.register_callbacks(app)


if __name__ == '__main__':
    #app.run_server(debug=True)
    app.run_server(host="0.0.0.0", port=8080)
