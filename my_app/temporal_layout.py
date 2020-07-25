import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import datetime as dt

# df = pd.read_csv('data/news_categorized.csv', nrows=100)
# df['fecha_publicacion']=pd.to_datetime(df['fecha_publicacion'])
# df['year']=df['fecha_publicacion'].dt.year
# df['week']=df['fecha_publicacion'].dt.week

lista_news_categoria_0 = []
lista_news_categoria_1 = []
lista_news_categoria_2 = []
lista_news_categoria_3 = []
tituloNotica = "Titulo noticia"
fechaNoticia = "Fecha noticia"
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
            value=-1
        )
        ], style={'border':'1px black solid'}),
    ]),
    dbc.Col(children=[
        html.Br(),
        html.H5("Agrupamiento 2"),
        html.Div(children=[
        dbc.RadioItems(options=lista_news_categoria_0,
            id="noticias_categoria_1",
            style={"overflow":"scroll","height":200},
            value=-1
        )
        ], style={'border':'1px black solid'}),
    ]),
    dbc.Col(children=[
        html.Br(),
        html.H5("Agrupamiento 3"),
        html.Div(children=[
        dbc.RadioItems(options=lista_news_categoria_0,
            id="noticias_categoria_2",
            style={"overflow":"scroll","height":200},
            value=-1
        )
        ], style={'border':'2px black solid'}),
    ]),
    dbc.Col(children=[
        html.Br(),
        html.H5("Agrupamiento 4"),
        html.Div(children=[
        dbc.RadioItems(options=lista_news_categoria_0,
            id="noticias_categoria_3",
            style={"overflow":"scroll","height":200},
            value=-1
        )
        ], style={'border':'1px black solid'}),
    ]),

])

# EL VISOR DE LA SELECCIÓN TEMPORAL Y LOGO
muestra_seleccion_temporal = dbc.Container(children=[
    html.Br(),
    html.P("""
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
    html.Br(),
    html.P("AQUI EL LOGO")
])

# ESTE ES EL VISOR DE LA NOTICIA
muestra_noticia = dbc.Container(children=[
    html.Br(),
    html.Div(children=[
        html.H3(
            "Titulo noticia",
            style={'text-align':'center',
                'width':'auto',
                'offset':1},
            id="Titulo noticia"
        ),
        dbc.Row(children=[
            dbc.Col(
                dcc.Markdown('**Fecha:**'),
                width={'size':'auto', 'offset':1}
            ),
            dbc.Col(html.P("fecha noticia",
                            id="fecha noticia"))
        ]),
        dbc.Row(children=[
            dbc.Col(
                dcc.Markdown("cuerpo noticia",
                            id="cuerpo noticia",
                            style={"overflow":"scroll",
                            "height":150,
                            "width":'auto'}),
                width={'size':10, 'offset':1}
            ),
            dbc.Col(width=1)
        ]),
        dbc.Row(children=[
            dbc.Col
                (
                    dcc.Link(children="hipervinculo",
                            href='',
                            target="_blank",
                            id="vinculo noticia"),
                    width={'size':400, 'offset':1}
                ),
        ])
    ],# style={'border':'2px black solid'},#, 'display':'block'},
    id='mostrar_noticia')
]
)

# ESTE ES EL VISUALIZADOR DE LAS PROBABILIDADES
muestra_probabilidades = dbc.Container(children=[
    dbc.Col(children=[
        html.P("AQUI LAS\nPROBABILIDADES")
    ])
])

##################################################################
# CUERPO DE LA PÁGINA
##################################################################

content = dbc.Container(children=[
    # EL LAYOUT ESTÁ PENSADO EN DOS FILAS
    # PRIMERA FILA CONTIENE EL GRAFICO
    # SEGUNDA FILA CONTIENE LAS CUATRO CATEGORIAS
    html.Br(),
    html.H3("Exploración de noticias"),
    html.Br(),
    dbc.Col(children=[
        html.P("""
            En esta página usted puede explorar las noticias más relevantes
            y aprovechar las clasificaciones sugeridas en su proceso de
            búsqueda de eventos relevantes.
            """
        ),
    ],
        width={'size':'50', 'offset':0}
    ),
    html.Br(),
    dbc.Row(children=[
        dbc.Col(
            muestra_seleccion_temporal
        ),
        dbc.Col(children=[
            html.Div(children=[
                muestra_noticia
            ],
            style={'width':500,
                    'height':400,
                    'border':'2px black solid',
                    'display':'block'
                    },
            )
        ]),
        dbc.Col(
            muestra_probabilidades
        )]
    ),
    dbc.Row(
        muestra_categorias
    )
], style = {'height':'500vh'})
