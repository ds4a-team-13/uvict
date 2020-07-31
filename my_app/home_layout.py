import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

##################################################################
# PARTES DE LA PÁGINA
##################################################################

# ESTE ES EL VISOR DE LOS BOTONES PARA IR A LAS PAGINAS

muestra_botones = dbc.Container(children=[
    dbc.Row(children=[
        dbc.Button("Modelo de clasificación", color="primary",\
                    className="mr-1", id="boton_modelo", n_clicks=None),
        dbc.Button("Revisión de noticias", color="primary",\
                    className="mr-1", id="boton_revision", n_clicks=None),
        dbc.Button("Visualización", color="primary",\
                    className="mr-1", id="boton_visualizacion", n_clicks=None)
    ])
])

##################################################################
# CUERPO DE LA PÁGINA
##################################################################

content = dbc.Container(children=[
    html.Br(),
    dbc.Row(children=[
        dbc.Col(children=[
            html.Div(id='none',children=[],style={'display': 'none'}),
            ], id="logo"
            ),
        dbc.Col("""
            Sistema de recomendación de noticias para la Bitácora
            de Eventos Diarios de la Unidad de Víctimas
            """)
    ]),
    html.Br(),
    dbc.Row(
        muestra_botones
    ),
], style = {'height':'500vh'})
