import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import datetime as dt
import dash_daq as daq
import os
import base64

# path = os.path.dirname(os.path.abspath(__file__))
# imagen = path + '/imagenes/c1_logo.jpeg'
# imagen = 'c1_logo.jpeg'
image_filename = 'c1_logo.jpeg'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

lista_news_categoria_0 = []
lista_news_categoria_1 = []
lista_news_categoria_2 = []
lista_news_categoria_3 = []
tituloNotica = "Titulo noticia"
fechaNoticia = " Fecha noticia"
cuerpoNoticia = "Cuerpo noticia"
urlNoticia = ""
valor_lista_cat_0 = -1
valor_lista_cat_1 = -1
valor_lista_cat_2 = -1
valor_lista_cat_3 = -1

##################################################################
# PARTES DE LA PÁGINA
##################################################################

# ESTE ES EL VISOR DE LAS CATEGORÍAS
muestra_categorias = dbc.Row(children=[
    dbc.Col(children=[
        html.Br(),
        html.H5("Agrupamiento 1"),
        html.Div(children=[
        dbc.RadioItems(options=lista_news_categoria_0,
            id="noticias_categoria_0",
            style={"overflow":"scroll","height":200},
            value=valor_lista_cat_0
        )
        ], style={'border':'4px black solid',
                'border-color': '#375A80'
                }),
    ]),
    dbc.Col(children=[
        html.Br(),
        html.H5("Agrupamiento 2"),
        html.Div(children=[
        dbc.RadioItems(options=lista_news_categoria_0,
            id="noticias_categoria_1",
            style={"overflow":"scroll","height":200},
            value=valor_lista_cat_1
        )
        ], style={'border':'4px black solid',
                'border-color': '#375A80'
                }),
    ]),
    dbc.Col(children=[
        html.Br(),
        html.H5("Agrupamiento 3"),
        html.Div(children=[
        dbc.RadioItems(options=lista_news_categoria_0,
            id="noticias_categoria_2",
            style={"overflow":"scroll","height":200},
            value=valor_lista_cat_2
        )
        ], style={'border':'4px black solid',
                'border-color': '#375A80'
                }),
    ]),
    dbc.Col(children=[
        html.Br(),
        html.H5("Agrupamiento 4"),
        html.Div(children=[
        dbc.RadioItems(options=lista_news_categoria_0,
            id="noticias_categoria_3",
            style={"overflow":"scroll","height":200},
            value=valor_lista_cat_3
        )
        ], style={'border':'4px black solid',
                'border-color': '#375A80'
                }),
    ]),

])

# EL VISOR DE LA SELECCIÓN TEMPORAL
muestra_seleccion_temporal = dbc.Container(children=[
    dbc.Row(children=[
        dbc.Col(children=[
            html.H6("""
                Seleccione el intervalo temporal para iniciar la exploración.
                """),
            html.Br(),
            dbc.FormGroup([
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=dt(2012, 1, 1),
                    max_date_allowed=dt(2020, 6, 30),
                    initial_visible_month=dt(2019, 1, 1),
                    start_date=dt(2018, 12, 1).date(),
                    end_date=dt(2019, 1, 7).date()
                ),
                html.Div(id='output-container-date-picker-range')
            ]),
        ])
    ])
])

# ESTE ES EL VISOR DE LA NOTICIA
muestra_noticia = dbc.Container(children=[
#    html.Br(),
    dbc.Col(children=[
        html.H3(
            "Titulo noticia",
            style={'text-align':'center'},
            id="Titulo noticia"
        ),
        dbc.Row(children=[
            dcc.Markdown('**Fecha:  **'),
            html.P("fecha noticia", id="fecha noticia")
        ]),
        dbc.Row(children=[
            dbc.Col(
                dcc.Markdown("cuerpo noticia",
                            id="cuerpo noticia",
                            style={"overflow":"scroll",
                            'textAlign':'justify',
                            "height":150,
                            "width":'auto'})
            )
        ]),
        dbc.Row(children=[
            dbc.Col
                (children=[
                    html.Br(),
                    dcc.Link(children="hipervinculo",
                            href='',
                            target="_blank",
                            id="vinculo noticia")
                ]),
        ])
    ],
    id='mostrar_noticia')
]
)

# ESTE ES EL VISUALIZADOR DE LAS PROBABILIDADES
muestra_probabilidades = dbc.Container(children=[
    dbc.Col(children=[
        dbc.Row(children=[
            daq.Gauge(min=0, max=100, value=6,
                color=theme['primary'],
                id='gauge-cat0',
                className='dark-theme-control',
                label="Acciones armadas",
                units="MPH",
                size=150),
            daq.Gauge(min=0, max=100, value=84,
                color=theme['primary'],
                id='gauge-cat1',
                className='dark-theme-control',
                label="Acciones contra la población civil",
                units="%",
                size=150),
        ]),
        dbc.Row(children=[
            daq.Gauge(min=0, max=100, value=20,
                color=theme['primary'],
                id='gauge-cat2',
                className='dark-theme-control',
                label="Acciones institucionales",
                units="Km/h",
                size=150),
            daq.Gauge(min=0, max=100, value=60,
                color=theme['primary'],
                id='gauge-cat3',
                className='dark-theme-control',
                label="Otros hechos",
                units="%",
                size=150),
        ])
    ])
])

##################################################################
# CUERPO DE LA PÁGINA
##################################################################

content = dbc.Container(children=[
    html.Br(),
    dbc.Row(html.H3("Revisión de noticias")),
    html.Br(),
    dbc.Row(children=[
        dbc.Col(
            html.H5("""
                En esta página usted puede explorar las noticias que han
                sido agrupadas inteligentemente por el sistema automático.
                Cuando se seleccione una noticia de uno de los agrupamientos,
                en los tacómetros se presentará una probabilidad de afinidad
                con los cuatro tipos de hechos que son relevantes para la
                Unidad de Víctimas, de tal manera que se facilite el proceso
                de clasificación para la Bitácora Diaria de Eventos.
                """,
                style={'textAlign':'justify'}
            ),
        ),
        dbc.Col(
            # html.Div(style={'backgroundImage': 'url(https://github.com/Slendercoder/DS4A-Dash-Draft/blob/master/c1_logo.png)'})
            # html.Img(src='data:imagenes/png;base64,{}'.format(encoded_image))
            html.Img(src='https://github.com/Slendercoder/DS4A-Dash-Draft/blob/master/c1_logo.png',\
                width=200)
            )
    ]),
    html.Br(),
    dbc.Row(
        muestra_seleccion_temporal
    ),
    dbc.Row(
        muestra_categorias
    ),
    html.Br(),
    dbc.Row(children=[
        dbc.Col(children=[
                muestra_noticia
            ],
            style={'width':'auto',
                    'height':400,
                    'border':'4px black solid',
                    'border-color': '#375A80',
                    'display':'block'
                    }
            ),
        dbc.Col(children=[
            muestra_probabilidades
        ],
        style={'width':'auto',
                'height':400,
                'border':'4px black solid',
                'border-color': '#375A80',
                'display':'block'
                }
        )]
    )
], style = {'height':'500vh'})
