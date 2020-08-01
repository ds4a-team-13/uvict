import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import State, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd


######## COMPONENTS

paragraph1 = "Este sitio es una herramienta diseñada para mejorar la intervención humanitaria de emergencia del Estado. Se pretende apoyar al personal profesional de la Unidad de Víctimas en la actualización de una bitacora de eventos, identificando, recopilando y clasificando los eventos relacionados con la dinámica de la violencia del conflicto armado que se informa en los noticieros nacionales y locales. Esta herramienta de aprendizaje automático recoge noticias digitales y las relaciona con una probabilidad de categorización en algunos de los eventos victimizantes."

hechos = ["Hechos contra la población","Acciones armadas","Acciones Institucionales","Otros tipos"]

section2 = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Row([
                dbc.Col(html.Div(
                [
                    html.Div(
                        [
                            html.P(paragraph1, style={'textAlign':'justify'}),
                            html.P("Las cuatro categorías de hechos victimizantes que maneja la Unidad de Víctimas son las siguientes (ver imagen):"),
                            html.Ul(id='my-list', children=[html.Li(i) for i in hechos])
                        ]
                    )
                ],),md=6),
                dbc.Col(html.Div(id="categorias"),md=6)
                ])
            ]
        ),
    ],
    body=True,
)


section3 = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Row([
                html.P("La presente herramienta de apoyo genera, en primer lugar, unos agrupamientos basados en similitudes entre las noticias.",\
                style={'textAlign':'justify'}),
                html.P("Con base en la similitud semántica entre las palabras que componen a cada noticia, se generaron 8 agrupamientos. En la siguiente figura se muestra, en el panel de la derecha una imagen donde cada punto es una noticia en el espacio semántico, y los colores codifican los agrupamientos. Para cada uno de ellos se incluye, en el panel de la derecha, una nube de palabras, la cual ayuda a describir el contenido de las noticas.",\
                style={'textAlign':'justify'}),
                dbc.Col(html.Div(id="umap"),md=6),
                dbc.Col(html.Div(id="wordclouds"),md=6),
                html.P("Los agrupamientos más importantes en referencia a las cuatro categorías de la Unidad de Víctimas son el 2, 4, 5 y 7. A partir de la nube de palabras, los hemos descrito como \'Narcotráfico\', \'Contrabando\', \'Grupos armados\' y \'Delitos sexuales\'.",\
                style={'textAlign':'justify'})                                ])
            ]
        ),
    ],
    body=True,
)


section4 = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Row([
                html.P("Sobre los diarios, las siguientes gráficas muestan una breve descripción de la información que se pudo obtener de ellos para los análisis realizados:"),
                dbc.Col(html.Div(id="boxplot"),md=6),
                dbc.Col(html.Div(id="serie"),md=6)
                ])
            ]
        ),
    ],
    body=True,
)



###### VISUALIZATION
content = dbc.Container(
    [
        html.Div(id='none',children=[],style={'display': 'none'}),
        dbc.Row([section2],align="center",),
        dbc.Row([section4],align="center",),
        dbc.Row([section3],align="center",),
    ],
    fluid=True,
)
